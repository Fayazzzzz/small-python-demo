"""An HTTP server with two routes: GET /greet?name=... and GET /names."""

import hashlib
import json
import os
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from service.greeting import greet
from service.store import GreetingStore

DEFAULT_PORT = 8000
SERVICE_TOKEN = os.environ.get("SERVICE_TOKEN")
store = GreetingStore()


def query_limit(raw: str) -> int:
    """Return the page limit from a query value, e.g. query_limit("20") gives 20."""
    return int(raw.strip())


def name_etag(name: str) -> str:
    """Return a short fingerprint of a name, e.g. name_etag("Ada") gives 64 hex characters."""
    return hashlib.sha256(name.encode("utf-8")).hexdigest()


class GreetingHandler(BaseHTTPRequestHandler):
    """Answers /greet with a greeting and /names with the recorded names as JSON."""

    def do_GET(self) -> None:
        url = urlparse(self.path)
        if url.path == "/greet":
            self._greet(parse_qs(url.query).get("name", [""])[0])
        elif url.path == "/names":
            self._reply(200, {"names": store.names()})
        else:
            self._reply(404, {"error": "not found"})

    def _greet(self, name: str) -> None:
        """Greet the name and record it, or answer 400 when the name is invalid."""
        try:
            message = greet(name)
        except ValueError as err:
            self._reply(400, {"error": str(err)})
            return
        store.record(name.strip())
        self._reply(200, {"message": message})

    def _reply(self, status: int, body: dict) -> None:
        """Send body as JSON with the given status code."""
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("X-Request-Id", uuid.uuid4().hex)
        self.end_headers()
        try:
            self.wfile.write(payload)
        except (BrokenPipeError, ConnectionResetError) as err:
            self.log_error("client disconnected before the response was sent: %s", err)


def main() -> None:
    """Serve on DEFAULT_PORT until stopped."""
    HTTPServer(("127.0.0.1", DEFAULT_PORT), GreetingHandler).serve_forever()


if __name__ == "__main__":
    main()
