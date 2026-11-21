# FastAPI Authentication and Authorization

This folder contains a runnable example API demonstrating username/password
login, password hashing, signed JWT access tokens, and role-based authorization.
The authentication-versus-authorization diagram in this folder illustrates the
same flow.

## Architecture

```text
Client
  | POST /auth/login (JSON username + password)
  v
Routes -> UserRepository (SQLite) -> verify Argon2 password hash
  | signed, short-lived JWT
  v
Client -- Authorization: Bearer <token> --> Protected route
                                           | validate JWT and load user
                                           | verify role when required
                                           v
                                      response or 401/403
```

The code is split into small layers:

- `app/routes.py` defines HTTP endpoints and translates application results to
  HTTP responses.
- `app/dependencies.py` authenticates bearer tokens and provides reusable role
  checks.
- `app/security.py` hashes and verifies passwords and creates/validates JWTs.
- `app/repository.py` persists user accounts in SQLite.
- `app/domain.py` contains the user record and supported roles.
- `app/schemas.py` defines validated request and response data.
- `app/config.py` reads secrets and runtime settings from environment variables.
- `app/main.py` assembles the FastAPI application and initializes the database.
- `app/create_user.py` is the command-line account provisioning tool.

For the detailed request flow and security decisions, see
[ARCHITECTURE.md](./ARCHITECTURE.md).

## Requirements and setup

Use Python 3.9 or newer. From this folder, create and activate a virtual
environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the application and test dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Set a signing key of at least 32 characters. Keep it private and do not commit
it to source control:

```bash
export JWT_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
```

On Windows PowerShell:

```powershell
$env:JWT_SECRET_KEY = python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Optional settings:

```bash
export DATABASE_PATH=./auth.db
export ACCESS_TOKEN_MINUTES=15
```

`DATABASE_PATH` defaults to `auth.db` in the current working directory.
`ACCESS_TOKEN_MINUTES` defaults to 15.

## Create an account and run the API

Create a regular user. The password is prompted securely and must be at least
12 characters:

```bash
python -m app.create_user --username alice
```

To create an administrator, use `--role admin`. Only trusted operators should
have permission to run this command.

Run the development server from this folder:

```bash
uvicorn app.main:app --reload
```

Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## API examples

### 1. Log in

Send JSON to `POST /auth/login`:

```json
{
  "username": "alice",
  "password": "your-password"
}
```

The response contains an `access_token`, its `token_type` (`bearer`), and
`expires_in` seconds. A bad username or password returns `401 Unauthorized`
with a generic message.

### 2. Authenticate

Send the token in the `Authorization` header to `GET /users/me`:

```http
Authorization: Bearer <access_token>
```

Without a valid token, a protected endpoint returns `401 Unauthorized`.

### 3. Authorize

`GET /admin/dashboard` requires the `admin` role. A signed-in `user` receives
`403 Forbidden`; an `admin` can access it. Roles are loaded from SQLite on each
request, so a role change takes effect immediately without waiting for the
access token to expire.

## Run tests

With the virtual environment activated and development dependencies installed:

```bash
pytest
```

## Security notes

- Passwords are stored as Argon2 hashes using `pwdlib`; raw passwords are never
  stored or returned.
- JWTs are signed, not encrypted. Their claims can be read by anyone holding
  the token; never put passwords, signing keys, or other secrets in a token.
- The API accepts a fixed signing algorithm and validates token expiry and
  subject. Access tokens expire after a short configured interval.
- The JWT signing key is supplied through the environment and has no built-in
  default. Use a secret manager and HTTPS for deployed services.
- SQLite is suitable for this learning example and a single-process demo.
  Production systems should consider a managed database, refresh-token and
  revocation strategy, rate limiting, audit logging, and operational secret
  rotation.
