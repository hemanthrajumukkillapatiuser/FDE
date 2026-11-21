from typing import Any

from fastapi import FastAPI, Request

app = FastAPI(title="HTTP Operations Demo")


def request_details(request: Request) -> dict[str, Any]:
    return {
        "method": request.method,
        "path": request.url.path,
        "query": dict(request.query_params),
    }


@app.get("/demo")
async def get_demo(request: Request):
    return {
        "message": "This is a GET response",
        **request_details(request),
    }


@app.post("/demo")
async def post_demo(payload: dict[str, Any]):
    return {
        "message": "Received a POST request",
        "data": payload,
    }


@app.put("/demo")
async def put_demo(payload: dict[str, Any]):
    return {
        "message": "Received a PUT request",
        "data": payload,
    }


@app.patch("/demo")
async def patch_demo(payload: dict[str, Any]):
    return {
        "message": "Received a PATCH request",
        "data": payload,
    }


@app.delete("/demo")
async def delete_demo(request: Request):
    return {
        "message": "Received a DELETE request",
        **request_details(request),
    }
