from flask import jsonify
import json
from data.conexion import container_client
from azure.core.exceptions import ResourceNotFoundError

class AccessDataFromAzure():

  @classmethod
  def verifyExistFile(cls, client):
    try:
      client.get_blob_properties()
      return 'El archivo existe'
    except:
      return 'El archivo no existe'

  @classmethod
  def access_data(cls, namefile):
    blob_client = container_client.get_blob_client(namefile)

    try:
      blob_data = blob_client.download_blob()
      file_content = blob_data.readall()
      # print(file_content)
      file_json = json.loads(file_content)
      return jsonify(file_json)
    except ResourceNotFoundError as e:
      return f'Error al acceder al archivo: {str(e)}'
    except Exception as e:
      return f'Otro error inesperado: {str(e)}'
    