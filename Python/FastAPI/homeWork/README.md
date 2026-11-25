# User CRUD API

A FastAPI application that reads and writes user records in the `users.json`
file in the parent folder. It uses no database.

## Run the API

From the `Python/FastAPI` folder, run:

```bash
python3 -m pip install -r requirements.txt
python3 -m uvicorn homeWork.user_operation:app --host 127.0.0.1 --port 8000 --reload
```

Open [Swagger UI](http://127.0.0.1:8000/docs) to try the endpoints.

## Endpoints

| Method | URL | Behavior |
| --- | --- | --- |
| `GET` | `/users` | Return all users |
| `GET` | `/users/{user_id}` | Return one user |
| `POST` | `/users` | Add a user; assign the next ID if omitted |
| `PUT` | `/users/{user_id}` | Replace a user |
| `PATCH` | `/users/{user_id}` | Update the provided user fields |
| `DELETE` | `/users/{user_id}` | Delete and return a user |

`PUT` and `PATCH` require a JSON object in the request body. For example:

```json
{
  "name": "Ada Lovelace",
  "email": "ada@example.com"
}
```

The API returns `404` when a requested user does not exist and `409` when a
`POST` request specifies an ID that is already in use. Changes are saved to
`users.json` immediately.
