#!/usr/bin/env python3
"""
A simple HTTP server using Python's http.server module.

Features:
- Handle GET requests
- Return text and JSON responses
- Support multiple endpoints
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom handler for a basic RESTful API."""

    def do_GET(self):
        """Handle GET requests for different endpoints."""

        # --- ROOT ENDPOINT ---
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Hello, this is a simple API!")
        
        # --- /data ENDPOINT ---
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_str = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json_str.encode("utf-8"))

        # --- /status ENDPOINT ---
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"OK")

        # --- /info ENDPOINT ---
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            json_str = json.dumps(info)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json_str.encode("utf-8"))

        # --- UNKNOWN ENDPOINTS ---
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Endpoint not found")


def run_server():
    """Start the HTTP server on port 8000."""
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)

    print("Server running on http://localhost:8000 ...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
