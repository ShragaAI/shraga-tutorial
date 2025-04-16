## Shraga Tutprial

The backend is based on FastAPI and frontend is based on React.

## Backend setup:

Requirements:

1. Python3.11
2. Pip
3. Poetry

To install poetry and add it to $PATH run

```bash
pipx install poetry
```

Once poetry is installed, install dependencies:

```bash
poetry install --no-root
```

To activate the virtualenv run the following:

```bash
poetry shell
which python
```

## Running the app

To run the app use:

```bash
SHRAGA_FLOWS_PATH=flows CONFIG_PATH=config.demo.yaml uvicorn main:app --reload
```

In a separate terminal run 
```
cd frontend
pnpm install
pnpm run dev

```

## Adding flows to the demo

In `main.py` the application is initialized with a default list of flows, imported from `shraga_common.flows.demo`.
You can implement your own flows inside the `flows` directory and add them to the list of flows in `main.py`.