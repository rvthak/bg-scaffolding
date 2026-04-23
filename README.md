# bg-scaffolding

Minimal Python service scaffold for a live coding interview. All layers are wired together and working out of the box — replace the placeholder logic to solve the problem.

## Project layout

```
bg-scaffolding/
├── src/
│   ├── api.py           # Flask routes (wired to service layer)
│   ├── cli.py           # Click CLI (wired to service layer)
│   ├── errors.py        # custom exceptions
│   ├── models.py        # domain model (Item dataclass)
│   ├── service.py       # business logic layer
│   └── store.py         # SQLite data store
├── tests/
│   └── test_app.py      # pytest tests
├── main.py              # entry point — starts Flask on port 8080
└── requirements.txt
```

## Setup

### 1. Create and activate the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the server

```bash
python main.py
# Server starts at http://localhost:8080
```

Endpoints:
- `GET /health`        → `{"status": "ok"}`
- `GET /items`         → `[]`
- `GET /items/<id>`    → `{"id": 1, "name": "..."}`

## Running the CLI

```bash
python -m src.cli list          # list all items
python -m src.cli get <id>      # get item by ID
python -m src.cli reset         # reset the database
```

## Running the tests

```bash
python -m pytest -v
```
