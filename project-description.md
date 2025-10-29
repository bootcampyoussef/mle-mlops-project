# MLOps Project

## Project Description

In this project you will create a GitHub Action that trains the model we trained during the intro to Evidently and uses DVC for the versioning of the train data. This model should be used in an API (you can take the one from yesterday). 
You should monitor the API and the model using Evidently, Prometheus and Grafana.

## Project Structure

The project structure is as follows:

- Take the code from the training notebook and put it into a python file 
- Create a GitHub Action that trains the model, tracks it with MLflow and uses DVC for the versioning of the train data
- Update the API that uses this model and deploy the API
- Monitor the API and the model using Evidently, Prometheus and Grafana


Bonus 1: Send data to the API and monitor the data with Evidently
Bonus 2: Use the GitHub Action to retrain the model with new data if you see data drift 

## How to submit your project

Upload your project on GitHub and send us the link.
