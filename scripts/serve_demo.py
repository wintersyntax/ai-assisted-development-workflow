#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo"
os.chdir(DEMO)

server = ThreadingHTTPServer(("127.0.0.1", 8767), SimpleHTTPRequestHandler)
print("Workflow demo: http://127.0.0.1:8767")
print("Synthetic data only. Press Ctrl+C to stop.")
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
