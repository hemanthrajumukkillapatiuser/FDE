# FastAPI HTTP Operations Demo

A small FastAPI demo that shows basic `GET`, `POST`, `PUT`, `PATCH`, and
`DELETE` operations. It does not use a database or backend; request data is
returned directly in the response.

## Requirements

- Python 3.9 or newer
- Pip

## Installation

From this folder, install the dependencies:

```bash
cd /Users/jeevantiwari/Desktop/FDE/Python/FastAPI
python3 -m pip install -r requirements.txt
```

## Run locally

```bash
python3 -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Keep the terminal running while using the API.

- Swagger UI: http://127.0.0.1:8000/docs
- Demo endpoint: http://127.0.0.1:8000/demo

Stop the server with `Ctrl+C`.

## Available endpoints

All operations use `/demo`.

| Method | URL | Request body |
| --- | --- | --- |
| `GET` | `/demo?name=test` | Not required |
| `POST` | `/demo` | JSON |
| `PUT` | `/demo` | JSON |
| `PATCH` | `/demo` | JSON |
| `DELETE` | `/demo?name=test` | Not required |

## Try the operations in Postman

Set the base URL to:

```text
http://127.0.0.1:8000
```

### GET

Select `GET` and open:

```text
http://127.0.0.1:8000/demo?name=test
```

Example response:

```json
{
  "message": "This is a GET response",
  "method": "GET",
  "path": "/demo",
  "query": {
    "name": "test"
  }
}
```

### POST

Select `POST`, open `http://127.0.0.1:8000/demo`, and set:

- **Body**
- **raw**
- **JSON**

```json
{
  "name": "Ada",
  "age": 36
}
```

The response contains the submitted JSON in `data`.

### PUT

Select `PUT`, open `http://127.0.0.1:8000/demo`, and send JSON in the body:

```json
{
  "name": "Ada",
  "age": 36
}
```

The response contains the submitted JSON in `data`.

### PATCH

Select `PATCH`, open `http://127.0.0.1:8000/demo`, and send JSON in the body:

```json
{
  "age": 37
}
```

The response contains the submitted JSON in `data`.

### DELETE

Select `DELETE` and open:

```text
http://127.0.0.1:8000/demo?name=test
```

The response includes the delete method, path, and query parameters.
