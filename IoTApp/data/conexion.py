from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import os

load_dotenv()

connect_str = os.getenv('AZURE_STORAGE_CONNECT_STRING')
container_name = os.getenv('AZURE_CONTAINER_BLOB') 