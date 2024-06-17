from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()

connect_str = os.getenv('AZURE_STORAGE_CONNECT_STRING')
container_name = os.getenv('AZURE_CONTAINER_BLOB')

if not connect_str or not container_name:
  raise ValueError('Las variables necesarias no han sido cargadas')

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)