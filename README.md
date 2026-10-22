# Small python demo

A greeting service written in Python with only the standard library, so it needs no installs.

## What it does

The service runs an HTTP server on port 8000 with two routes:

- `GET /greet?name=Ada` returns `{"message": "Hello, Ada!"}`. Names must be letters and spaces, up to 50 characters, otherwise the service returns 400. Each greeted name is remembered.
- `GET /names` returns the names greeted so far, in the order first seen, e.g. `{"names": ["Ada", "Grace"]}`.

Any other path returns 404.

## Layout

- `service/greeting.py` builds the greeting text.
- `service/validators.py` checks names.
- `service/store.py` remembers greeted names in memory, so they are lost when the server stops.
- `service/server.py` is the HTTP server.
- `tests/test_service.py` holds the unit tests.

## Run it

```
python3 -m service.server
curl "http://127.0.0.1:8000/greet?name=Ada"
```

## Test it

```
python3 -m unittest tests.test_service
```
