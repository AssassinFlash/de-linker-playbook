#!/usr/bin/env python3
"""Serve the React ops dashboard and open it in a browser.

Prefers 127.0.0.1:8766. If that port is taken, uses the next free port.
If this app is already running, just opens the existing page.
"""
from __future__ import annotations

import json
import os
import socket
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "apps" / "ops-dashboard" / "dist"
DATA = Path.home() / ".config" / "de-linker-playbook" / "dashboard.json"
LOCK = Path.home() / ".config" / "de-linker-playbook" / "ops-dashboard.port"
HOST = "127.0.0.1"
PREFERRED = 8766


def port_open(port: int) -> bool:
    probe = socket.socket()
    probe.settimeout(0.3)
    try:
        probe.connect((HOST, port))
        return True
    except OSError:
        return False
    finally:
        probe.close()


def running_port() -> int | None:
    if not LOCK.exists():
        return None
    text = LOCK.read_text(encoding="utf-8").strip()
    if not text.isdigit():
        return None
    port = int(text)
    return port if port_open(port) else None


def free_port() -> int:
    for port in range(PREFERRED, PREFERRED + 30):
        if port_open(port):
            continue
        probe = socket.socket()
        try:
            probe.bind((HOST, port))
            return port
        except OSError:
            continue
        finally:
            probe.close()
    raise SystemExit("8766 到 8795 都被占用了")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        return

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]
        if path == "/data.json":
            if not DATA.exists():
                body = "还没有导出。先运行 uv run scripts/dashboard.py export。".encode()
                self.send_response(404)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            payload = DATA.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        if path in ("/", "/index.html"):
            return super().do_GET()
        target = DIST / path.lstrip("/")
        if target.is_file():
            return super().do_GET()
        self.path = "/index.html"
        return super().do_GET()


def main() -> int:
    if not DIST.joinpath("index.html").exists():
        print(f"missing {DIST}; run the ops-dashboard launcher so it can build", file=sys.stderr)
        return 1
    existing = running_port()
    if existing:
        url = f"http://{HOST}:{existing}/"
        print(url, flush=True)
        if os.environ.get("OPS_DASHBOARD_NO_OPEN") != "1":
            webbrowser.open(url)
        return 0
    port = free_port()
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    LOCK.write_text(str(port), encoding="utf-8")
    os.chmod(LOCK, 0o600)
    server = ThreadingHTTPServer((HOST, port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = f"http://{HOST}:{port}/"
    print(url, flush=True)
    print("关掉这个窗口，看板就停。", flush=True)
    if os.environ.get("OPS_DASHBOARD_NO_OPEN") != "1":
        webbrowser.open(url)
    try:
        thread.join()
    except KeyboardInterrupt:
        server.shutdown()
    finally:
        LOCK.unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
