# Assemblief FastAPI Starter

A local-first FastAPI application skeleton with SQLite initialization, modular package layout, and a server-rendered dashboard.

## Quick start

```bash
pip install -r requirements.txt
python main.py
```

When started via `python main.py` the app will:

1. Configure logging
2. Initialize SQLite at `app/data/assemblief.db`
3. Start a Uvicorn-powered FastAPI server
4. Attempt to open your default browser at `http://127.0.0.1:8000/`

## Routes

- `/` – institutional style dashboard (Jinja2 template)
- `/health` – JSON health status

## Configuration

Runtime config is managed through environment variables in `config.py`:

- `APP_NAME`
- `APP_HOST`
- `APP_PORT`
- `LOG_LEVEL`
- `DB_PATH`
