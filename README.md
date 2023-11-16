# CosmosDB Exporter
This project is a Python script that exports data from a CosmosDB container to a CSV file.

## Prerequisites
- Python 3.6 or higher
- Access to a CosmosDB instance
- Azure Cosmos DB SQL API SDK for Python
- python-dotenv module

## Installation

Install the Azure Cosmos DB SQL API SDK for Python:
```bash
pip install azure-cosmos
```
Install the python-dotenv module:

```bash
pip install python-dotenv
```

## Environment Variables
This project uses python-dotenv to load environment variables. Create a .env file in the project root and add the following variables:

- COSMOS_DB_ENDPOINT: Your CosmosDB endpoint.
- COSMOS_DB_KEY: Your CosmosDB key.
- COSMOS_DB_DATABASE: The database to export data from.
- COSMOS_DB_CONTAINER: The container to export data from.
- OUTPUT_FILE: The name of the output CSV file. If not provided, the default is 'cosmos_data.csv'.

## How to Use

Clone this repository to your local machine.


Navigate to the directory containing the `cosmos_exporter.py` script.
Set the environment variables in the .env file.

Run the script using Python.

```bash
python cosmos_exporter.py
```

This will create a CSV file (named as per the OUTPUT_FILE environment variable or 'cosmos_data.csv' by default) in the same directory, containing the exported data from the CosmosDB container.

### Note
The script determines all unique fields in the documents and writes the data to the CSV file accordingly. The CSV file is written in 'utf-8' encoding.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License MIT