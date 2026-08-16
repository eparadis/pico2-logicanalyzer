# Pico Logic Analyzer (Python)

This is the source-installed Python 3.12 Cycle 1 scaffold for one V2 Pico
logic analyzer. It deliberately exposes no serial or capture implementation
yet; C1-B2 through C1-B5 own those layers. The existing C# applications and
firmware remain the rollback and comparison paths.

From this directory, the canonical clean bootstrap is:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock
.venv/bin/python -m pip install --no-build-isolation --no-deps -e .
.venv/bin/python -m ruff check .
.venv/bin/python -m mypy src
.venv/bin/python -m pytest -m "not hardware"
.venv/bin/python -m pico_logic_analyzer --help
```

Do not connect a board until `docs/operator-input-template.md` has been
completed and the hardware batch is active. See `docs/device-protocol.md` for
the narrow, evidence-labelled protocol notes.

To update the lock deliberately, edit `requirements-dev.in` and regenerate it
with Python 3.12 and a current `pip-tools` installation:

```bash
pip-compile --upgrade --rebuild --allow-unsafe --strip-extras \
  --generate-hashes --output-file=requirements-dev.lock requirements-dev.in
```

Review dependency and hash changes before committing. The canonical bootstrap
must continue to install the lock with `--require-hashes` and install this
project with `--no-build-isolation --no-deps`.
