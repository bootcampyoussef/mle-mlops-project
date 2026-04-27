# MLOps Project

## Project Goal

Build a small but complete MLOps workflow around the model you trained during the Evidently introduction.

If you want a runnable baseline to compare your own work against, see the self-contained reference implementation in [solution/README.md](solution/README.md).

Your final project should show that you can move from experimentation to operations:

- training code is reusable outside a notebook;
- training data is versioned with DVC;
- model runs and artifacts are tracked with MLflow;
- retraining is automated with GitHub Actions;
- the trained model is served through an API;
- the API and model behavior are monitored with Evidently, Prometheus, and Grafana.

## Suggested Workflow

### 1. Refactor the training code

Objective:
Move the training logic out of the original notebook into Python files that can be executed repeatedly.

Suggested steps:

- create a small training entry point such as `src/train.py`;
- move preprocessing, training, and evaluation into reusable functions;
- save the trained artifact in a predictable location.

Deliverables:

- training code outside the notebook;
- a repeatable training command;
- a saved model artifact.

### 2. Track data and experiments

Objective:
Make the training inputs and outputs reproducible.

Suggested steps:

- version the training dataset with DVC;
- configure an MLflow experiment;
- log parameters, metrics, and model artifacts for each training run.

Deliverables:

- DVC metadata committed to the repository;
- an MLflow run showing at least one successful training execution.

Hints:

- keep the first DVC setup simple;
- track only the data needed to reproduce training.

### 3. Automate training with GitHub Actions

Objective:
Run the training pipeline automatically from CI.

Suggested steps:

- create a workflow that installs dependencies and runs the training script;
- make sure the workflow can access the data required for training;
- log the training run to MLflow as part of the workflow.

Deliverables:

- a working GitHub Actions workflow;
- evidence that the workflow completes successfully.

### 4. Serve the model through an API

Objective:
Expose the latest trained model through an inference endpoint.

Suggested steps:

- reuse or adapt the API you built previously;
- load the trained artifact on startup;
- add a prediction endpoint with a clear request and response schema.

Deliverables:

- runnable API code;
- an example request that returns a prediction.

### 5. Add monitoring

Objective:
Track both system behavior and model behavior.

Suggested steps:

- expose API metrics for Prometheus;
- create at least one Grafana dashboard;
- configure Evidently to monitor predictions, input data, or drift indicators.

Deliverables:

- visible Prometheus metrics;
- a Grafana dashboard with at least one useful panel;
- Evidently output or reports connected to your prediction flow.

## Suggested Architecture

You do not need to match this structure exactly, but a project like the following is usually easy to review:

```text
.
├── .github/workflows/
├── data/
├── src/
│   ├── train.py
│   ├── preprocess.py
│   └── api.py
├── monitoring/
├── models/
├── dvc.yaml
├── requirements.txt
└── README.md
```

## Minimum Acceptance Checklist

Your project should demonstrate all of the following:

- notebook training logic has been turned into reusable Python code;
- DVC is used for training data versioning;
- GitHub Actions can run the training pipeline;
- MLflow tracks the model training run;
- the trained model is available through an API;
- monitoring covers both operational metrics and model-related signals.

## Bonus Ideas

- send requests to the API and monitor the incoming data with Evidently;
- trigger retraining when you detect meaningful data drift;
- add a small smoke test for the API or training entry point.

## Submission

Upload your finished project to GitHub and share the repository link.
