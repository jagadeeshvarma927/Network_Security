
# Network Security ML Pipeline

This repository contains an end-to-end machine learning pipeline for network security analysis: data ingestion, validation, transformation, model training, evaluation, and model pusher. The project is organized to support reproducible experiments and CI-friendly automation.

## Key Features

- Modular components for each pipeline stage (ingestion, validation, transformation, training, evaluation, pusher).
- Artifact tracking under `Artifacts/` with timestamps for traceability.
- Configuration and entity abstractions for clean orchestration.
- Dockerfile for containerized execution.

## Quick Start

1. Create a Python environment and install dependencies:

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Run a training pipeline (example):

```bash
python main.py
```

Or run the training entrypoint:

```bash
python start_training.py
```

3. Inspect artifacts in the `Artifacts/` directory created with timestamps.

## Repository Structure

- `main.py` — entry point for running tasks or the pipeline.
- `start_training.py` — helper script to kick off training.
- `get_data.py`, `mongo_test.py` — data utilities and tests.
- `networksecurity/` — core Python package containing pipeline components and utilities:
	- `components/` — implementations of pipeline stages: `data_ingestion.py`, `data_transformation.py`, `data_validation.py`, `model_trainer.py`, `model_pusher.py`, `model_evaluation.py`.
	- `constant/` — project constants and pipeline configuration defaults.
	- `entity/` — dataclasses / entities used across the pipeline (`artifact_entity.py`, `config_entity.py`).
	- `exception/` — custom exceptions and error handling helpers.
	- `logger/` — logging setup utilities.
	- `pipeline/` — `training_pipeline.py` orchestrates the full pipeline.
	- `utils/` — assorted helpers: `main_utils/utils.py`, ML helpers, metrics and models.
- `Artifacts/` — produced artifacts grouped by timestamped runs: data ingestion outputs, transformed data, validation reports, trained models, evaluation reports, and pusher outputs.
- `data_schema/` — contains `schema.yaml` describing expected data schema.
- `Network_Data/` — sample or raw datasets like `network_data.csv`.
- `saved_models/` — persisted model directories.
- `Dockerfile` — containerization recipe.
- `requirements.txt`, `setup.py`, `LICENSE`, `README.md` — project metadata and dependencies.

## Data

- The canonical schema is at `data_schema/schema.yaml`.
- Place raw input CSVs in `Network_Data/` or configure your data source in the config entities.

## Running the Pipeline

Most orchestration is handled in `pipeline/training_pipeline.py` and invoked from `main.py` or `start_training.py`.

Example local run:

```bash
python start_training.py
```

Use the component modules to run specific stages individually for faster iteration. For example, to only run data ingestion, run the appropriate script or call the `DataIngestion` component from a short driver script.

## Docker

Build and run the Docker image:

```bash
docker build -t network-security-pipeline .
docker run --rm -v $(pwd)/Artifacts:/app/Artifacts network-security-pipeline
```

On Windows PowerShell, mount volumes like:

```powershell
docker run --rm -v ${PWD}:/app network-security-pipeline
```

## Logging

Logging is configured in `networksecurity/logger/logger.py`. Logs are written to the configured handlers; check the `logs/` folder for run-time logs.

## Configuration

Pipeline configuration objects live in `networksecurity/entity/config_entity.py` and constants in `networksecurity/constant/`. Adjust dataset paths, output directories, and hyperparameters there or via environment variables where supported.

## Artifacts and Outputs

- `Artifacts/<timestamp>/data_ingestion/` — raw ingested files and feature store.
- `Artifacts/<timestamp>/data_transformation/` — transformed datasets and transformer objects.
- `Artifacts/<timestamp>/data_validation/` — validation results and drift reports.
- `Artifacts/<timestamp>/model_trainer/` — trained model objects and training metadata.
- `Artifacts/<timestamp>/model_evaluation/` — evaluation reports (e.g., `report.yaml`).
- `Artifacts/<timestamp>/model_pusher/` — pushed model packages for deployment.

## Tests

There are no formal test harness files committed; add unit tests under a `tests/` directory and run with `pytest`.

## Contributing

1. Open an issue to discuss major changes.
2. Create a feature branch and submit a PR with clear description and tests where applicable.

## Troubleshooting

- If dependencies fail to install, ensure you are using a supported Python version (3.8+ recommended) and upgrade `pip`.
- Check logs in the `logs/` directory for stack traces.

## License

See the `LICENCE` file in the repository root.

---

If you'd like, I can also:
- add example commands to run each component individually,
- generate a minimal `examples/` driver script demonstrating a single end-to-end run,
- or open a PR with this README and run basic linting.
