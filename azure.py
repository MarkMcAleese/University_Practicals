from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Set your Azure subscription ID
subscription_id = 'YOUR_SUBSCRIPTION_ID'

# Authenticate using DefaultAzureCredential (assumes you've already configured your Azure credentials)
credential = DefaultAzureCredential()

# Create a Resource Management client
resource_client = ResourceManagementClient(credential, subscription_id)

# List all resource groups in the subscription
resource_groups = resource_client.resource_groups.list()

# Print the names of the resource groups
for rg in resource_groups:
    print(rg.name)