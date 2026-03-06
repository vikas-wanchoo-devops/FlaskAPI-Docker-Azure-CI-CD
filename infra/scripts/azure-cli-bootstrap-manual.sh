# Login and set subscription
az login
az account list --output table
az account set --subscription "Azure subscription 1"

# Resource group
az group create --name WanchooResourceGroup --location eastus

# Azure Container Registry (enable admin creds so you can use password later)
az acr create --resource-group WanchooResourceGroup --name vikasacr --sku Basic --admin-enabled true

# Register provider for Container Apps
az provider register --namespace Microsoft.App

# Container Apps environment
az containerapp env create \
  --name vikas-env \
  --resource-group WanchooResourceGroup \
  --location eastus