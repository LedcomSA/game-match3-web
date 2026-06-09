#!/usr/bin/env python3
"""
Serveur local pour tester l'export HTML5 Godot 4.
Ajoute les headers COOP/COEP requis pour SharedArrayBuffer.
Usage: python3 serve.py
"""
import http.server
import socketserver
import os

PORT = 8060
WEB_DIR = os.path.dirname(os.path.abspath(__file__))

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "cross-origin")
        super().end_headers()

    def log_message(self, format, *args):
        pass  # silencieux

with socketserver.TCPServer(("", PORT), CORSHandler) as httpd:
    print(f"Serveur démarré → http://localhost:{PORT}/index.html")
    print("Ctrl+C pour arrêter.")
    httpd.serve_forever()
