"""Validated App API access with a persistent last-known-good snapshot."""
import http.client
import json
import math
import os
from pathlib import Path
import tempfile
import urllib.request
from urllib.parse import urlparse

API_URLS = (
    "https://developer-category-api.dawei84.com/api/dawei",
    "https://app-store-developer-catalog-api.dwsamurai84.workers.dev/api/dawei",
)
ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = ROOT / ".cache/apps.json"
TIMEOUT = 15
FETCH_ERRORS = (OSError, ValueError, http.client.HTTPException)


def validate_apps(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list) or not payload["data"]:
        raise ValueError("App data must be a non-empty list")
    # Reject the entire snapshot instead of silently publishing a partial catalog.
    for app in payload["data"]:
        if not isinstance(app, dict):
            raise ValueError("App must be an object")
        for key in ("trackName", "trackViewUrl", "artworkUrl512"):
            if not isinstance(app.get(key), str) or not app[key].strip():
                raise ValueError(f"Missing or invalid {key}")
        for key in ("trackViewUrl", "artworkUrl512"):
            url = urlparse(app[key])
            if url.scheme != "https" or not url.netloc:
                raise ValueError(f"Invalid URL in {key}")
        if not isinstance(app.get("description", ""), str):
            raise ValueError("Invalid description")
        price = app.get("price", 0)
        if isinstance(price, bool) or not isinstance(price, (int, float)) or (isinstance(price, float) and not math.isfinite(price)) or price < 0:
            raise ValueError("Invalid price")
    return payload["data"]


def atomic_write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
            temporary = stream.name
            stream.write(text)
        os.replace(temporary, path)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def fetch_app_data(url):
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        payload = json.loads(response.read())
    validate_apps(payload)
    return payload


def load_apps():
    for url in API_URLS:
        try:
            payload = fetch_app_data(url)
        except FETCH_ERRORS as error:
            print(f"Warning: App API {url}: {type(error).__name__}: {error}")
            continue
        try:
            atomic_write(CACHE_PATH, json.dumps(payload, ensure_ascii=False))
        except OSError as error:
            print(f"Warning: could not save App cache: {error}")
        return payload["data"]
    try:
        apps = validate_apps(json.loads(CACHE_PATH.read_text(encoding="utf-8")))
        print("Warning: using last-known-good App cache")
        return apps
    except FETCH_ERRORS as error:
        print(f"Warning: no usable App cache: {error}")
        return None


def preserve_existing(path, card_class):
    """Without usable data, never replace a page; fail closed if none exists."""
    path = Path(path)
    if path.is_file() and f'class="{card_class}"' in path.read_text(encoding="utf-8"):
        print(f"Warning: preserving existing {path}")
        return
    raise RuntimeError(f"No usable data or existing content for {path}; stopping deployment")
