# my-python-project (demo)

A minimal Python project used as a build artifact for CI/containerization demos. The repository contains a tiny Python app that is tested with `pytest`, packaged into a Docker image, and built by GitHub Actions.

## Build & test locally

Install dependencies into a virtualenv and run tests:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q