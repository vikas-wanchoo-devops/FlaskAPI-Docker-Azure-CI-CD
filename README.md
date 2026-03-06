# 🚀 Flask API Deployment on Azure Container Apps


![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vikas-wanchoo-devops/FlaskAPI-Docker-Azure-CI-CD/docker.yml?branch=develop&cacheSeconds=60&timestamp=20260304)
![Docker Pulls](https://img.shields.io/docker/pulls/vikaswanchoo/flask-api?cacheSeconds=60&timestamp=20260304)
![GitHub Repo stars](https://img.shields.io/github/stars/vikas-wanchoo-devops/FlaskAPI-Docker-Azure-CI-CD?style=social&cacheSeconds=60&timestamp=20260304)
![GitHub License](https://img.shields.io/github/license/vikas-wanchoo-devops/FlaskAPI-Docker-Azure-CI-CD?cacheSeconds=60&timestamp=20260304)

## 📘 What this repo does
- 🔁 Simple Flask API application
- 📦 Builds and pushes Docker image to **Azure Container Registry (ACR)**
- ⚙️ Automated CI/CD pipeline using **GitHub Actions**
- ✅ Pipeline runs on every push to `main` branch
- 🌐 Deploys automatically to **Azure Container Apps** with a public URL

## 🧪 CI/CD Pipeline Steps
1. 📥 Checkout repository  
2. 🔐 Login to Azure using service principal  
3. 🏗️ Provision infra (manual run of `infra.yml`)  
4. 🐳 Build Docker image  
5. 📤 Push image to ACR  
6. ▶️ Deploy to Azure Container Apps  
7. 🔍 Output public URL for testing  
8. 🧹 Cleanup / scale operations (optional)

## 📂 Repository Structure
flask-api-deployment/
├── src/                  # Flask API source code
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── .github/workflows/    # CI/CD pipelines
│   ├── infra.yml         # Infra provisioning (manual run)
│   └── deploy.yml        # Build & deploy (auto run on push)
└── README.md             # Documentation

## 🛠️ Manual Commands

### 🏗️ Provision Infrastructure
az group create --name WanchooResourceGroup --location eastus
az acr create --resource-group WanchooResourceGroup --name vikasacr --sku Basic
az provider register -n Microsoft.App --wait
az provider register -n Microsoft.OperationalInsights --wait
az containerapp env create --name vikas-env --resource-group WanchooResourceGroup --location eastus

### 🐳 Build & Push Docker Image
az acr login --name vikasacr
docker build -t vikasacr.azurecr.io/flask-api:latest .
docker push vikasacr.azurecr.io/flask-api:latest
az acr repository list --name vikasacr --output table
az acr repository show-tags --name vikasacr --repository flask-api --output table

### ▶️ Deploy Container App
az containerapp create \
  --name flaskapi-app \
  --resource-group WanchooResourceGroup \
  --environment vikas-env \
  --image vikasacr.azurecr.io/flask-api:latest \
  --target-port 5000 \
  --ingress external \
  --registry-server vikasacr.azurecr.io \
  --registry-username vikasacr \
  --registry-password <ACR password>

### 🌐 Get Public URL
az containerapp show \
  --name flaskapi-app \
  --resource-group WanchooResourceGroup \
  --query properties.configuration.ingress.fqdn \
  --output table

## 🔍 Testing
curl https://flaskapi-app.<randomstring>.eastus.azurecontainerapps.io
curl https://flaskapi-app.<randomstring>.eastus.azurecontainerapps.io/hello

## ⚙️ Operations
az containerapp logs show --name flaskapi-app --resource-group WanchooResourceGroup --follow
az containerapp scale --name flaskapi-app --resource-group WanchooResourceGroup --min-replicas 1 --max-replicas 5

## ✅ Secrets Required
- AZURE_CREDENTIALS → Service principal JSON  
- ACR_PASSWORD → ACR admin password  

💡 Quick Start:  
1. Run infra.yml manually once to provision infra
