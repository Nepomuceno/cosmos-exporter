from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv
load_dotenv()
import csv
import os

# Azure Cosmos DB configuration
url = os.getenv('COSMOSDB_URL')
key = os.getenv('COSMOSDB_KEY')
database_name = os.getenv('COSMOSDB_DATABASE')
container_name = os.getenv('COSMOSDB_CONTAINER')

# Initialize Cosmos client
client = CosmosClient(url, credential=key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Query to select all documents in the container
query = "SELECT * FROM c"

# Fetching documents
items = list(container.query_items(query, enable_cross_partition_query=True))

# Fetching documents
items = list(container.query_items(query, enable_cross_partition_query=True))

# Determine all unique fields in the documents, excluding those that start with an underscore
fieldnames = set()
for item in items:
    fieldnames.update(key for key in item.keys() if not key.startswith('_'))
fieldnames = list(fieldnames)

# CSV file to save the data
output_file = 'cosmos_data.csv'

# Write data to CSV
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for item in items:
        # Filter out properties starting with an underscore
        filtered_data = {k: v for k, v in item.items() if not k.startswith('_')}
        writer.writerow(filtered_data)

print(f"Data exported to {output_file}")
