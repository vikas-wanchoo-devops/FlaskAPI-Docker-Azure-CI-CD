# Variables
$acrName = "vikasacr"
$imageName = "flask-api"

# Build tag string safely (force variable expansion)
$tag = "$($acrName).azurecr.io/$($imageName):latest"

# Validate variables before proceeding
if ([string]::IsNullOrWhiteSpace($acrName) -or [string]::IsNullOrWhiteSpace($imageName)) {
    Write-Error "ACR name or image name is empty. Please set both variables correctly."
    exit 1
}

Write-Output "Using tag: $tag"

# Get ACR credentials (username + password)
$acrCreds = az acr credential show --name $acrName | ConvertFrom-Json

# Login securely using password-stdin
$acrCreds.passwords[0].value | docker login "$acrName.azurecr.io" -u $acrCreds.username --password-stdin

# Build Docker image with 'latest' tag
docker build -t $tag .

# Push image to ACR
docker push $tag

# Verify image in ACR
az acr repository list --name $acrName --output table
az acr repository show-tags --name $acrName --repository $imageName --output table

# Optional sanity check: pull back the image locally
docker pull $tag