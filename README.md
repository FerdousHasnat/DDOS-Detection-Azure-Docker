# DDOS-Detection-Azure-Docker
This repository contains an AI-based DDOS detection system deployed on Azure using Docker.

## Overview
This project is an AI-Based Threat Detection System designed to identify and mitigate Distributed Denial-of-Service (DDoS) attacks. The system uses a Random Forest machine learning model to classify network traffic as malicious or benign. It integrates with Azure Machine Learning and Azure Container Instance (ACI) for deployment and provides a REST API endpoint for real-time predictions.

## Features
Data Preprocessing: Handles cleaning and feature engineering for network traffic data.
Machine Learning Model: Utilizes a Random Forest Classifier for high accuracy.
Docker Integration: Deploys the application as a Docker container for platform independence.
Azure Deployment: Uses Azure Container Instances (ACI) for cloud-based scalability.
REST API: Provides a Flask-based REST API for real-time DDoS detection.

## Setup Instructions
1. Clone the Repository
git clone https://github.com/username/repository-name.git
cd repository-name
git clone https://github.com/username/repository-name.git
cd repository-name

2. Install Dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Run Locally
Start the API Locally
python app/score.py

4.Test the API
python test_api.py

## Deployment
Build the Docker Image
docker build -t ddos-detection-api .

Run the Docker Container
docker run -p 5000:5000 ddos-detection-api

## Azure Deployment
Push the Docker Image to Azure Container Registry (ACR)
docker tag ddos-detection-api ddosdeteregistry.azurecr.io/ddos-detection-api:v1
docker push ddosdeteregistry.azurecr.io/ddos-detection-api:v1

## Deploy the Container on Azure:
az container create \
    --resource-group ddos-detection-group \
    --name ddos-detection-container \
    --image ddosdeteregistry.azurecr.io/ddos-detection-api:v1 \
    --cpu 1 \
    --memory 1 \
    --os-type Linux \
    --registry-login-server ddosdeteregistry.azurecr.io \
    --registry-username <your-acr-username> \
    --registry-password <your-acr-password> \
    --dns-name-label ddos-detection-service \
    --ports 5000

## Dataset 
Due to size limitations, the cleaned dataset is hosted externally. Download the cleaned DDOS dataset from https://drive.google.com/file/d/1yVT87Lv6pDxQN9YBu86CQDNHtdcrGLNy/view?usp=sharing

## REST API
Endpoint: /score
Method: POST
Request: JSON payload containing feature values.
Response: JSON object with predictions.

Example:
{
    "feature1": 123,
    "feature2": 45.6,
    "feature3": 78
}

## Key Features
Python: Core language for data processing and API development.
Scikit-learn: Machine learning framework.
Flask: API development.
Docker: Containerization for portability.
Azure: Cloud deployment and scalability.

## License 
This project is licensed under the MIT License
