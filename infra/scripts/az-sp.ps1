az ad sp create-for-rbac `
  --name "github-actions-sp" `
  --role contributor `
  --scopes /subscriptions/625b78b3-14cf-460c-81e6-d29c4eab3809/resourceGroups/WanchooResourceGroup `
  --sdk-auth
