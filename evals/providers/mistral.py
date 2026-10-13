#!/usr/bin/env python3
"""Small, explicit Mistral adapter for X001.

This module is deliberately side-effect free at import time. It does not select a
fallback model, read or print a secret, or make a network call unless a caller
explicitly invokes one of the request functions.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import requests


def load_api_key(root: Path) -> str | None:
    """Read MISTRAL_API_KEY from the environment or an ignored .env file."""
    if os.environ.get("MISTRAL_API_KEY"):
        return os.environ["MISTRAL_API_KEY"]
    env_path = root / ".env"
    if not env_path.exists():
        return None
    for line in env_path.read_text().splitlines():
        if line.startswith("MISTRAL_API_KEY="):
            value = line.split("=", 1)[1].strip().strip("'\"")
            return value or None
    return None


def _url(base_url: str, endpoint: str) -> str:
    return base_url.rstrip("/") + "/" + endpoint.lstrip("/")


def build_chat_request(model: str, messages: list[dict[str, str]], max_tokens: int,
                       temperature: float = 0.0, top_p: float = 1.0) -> dict[str, Any]:
    if not model:
        raise ValueError("X001 requires an explicitly pinned Mistral model")
    if not messages:
        raise ValueError("messages must not be empty")
    return {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "stream": False,
    }


def chat(base_url: str, api_key: str, model: str, messages: list[dict[str, str]],
         max_tokens: int, timeout: int = 180) -> dict[str, Any]:
    """Make one explicit chat call and return the decoded provider response."""
    if not api_key:
        raise ValueError("MISTRAL_API_KEY is required for a paid call")
    response = requests.post(
        _url(base_url, "/v1/chat/completions"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=build_chat_request(model, messages, max_tokens),
        timeout=timeout,
    )
    response.raise_for_status()
    payload = response.json()
    if not payload.get("choices"):
        raise ValueError("Mistral response contained no choices")
    return payload


def list_models(base_url: str, api_key: str, timeout: int = 30) -> list[dict[str, Any]]:
    """Fetch account-visible models for eligibility recording; no model is chosen here."""
    if not api_key:
        raise ValueError("MISTRAL_API_KEY is required for an account-scoped preflight")
    response = requests.get(
        _url(base_url, "/v1/models"),
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=timeout,
    )
    response.raise_for_status()
    payload = response.json()
    return payload.get("data", [])


def normalize_usage(payload: dict[str, Any]) -> dict[str, int]:
    """Normalize known usage fields while preserving zeroes for absent fields."""
    usage = payload.get("usage") or {}
    return {
        "prompt_tokens": int(usage.get("prompt_tokens", 0)),
        "completion_tokens": int(usage.get("completion_tokens", 0)),
        "total_tokens": int(usage.get("total_tokens", 0)),
        "prompt_cache_hit_tokens": int(usage.get("prompt_cache_hit_tokens", 0)),
        "prompt_cache_miss_tokens": int(usage.get("prompt_cache_miss_tokens", 0)),
    }


def assistant_text(payload: dict[str, Any]) -> str:
    """Extract plain text; reject unexpected structured content for this first pilot."""
    content = payload["choices"][0]["message"].get("content")
    if not isinstance(content, str):
        raise ValueError("X001 expects a plain-text assistant message")
    return content
