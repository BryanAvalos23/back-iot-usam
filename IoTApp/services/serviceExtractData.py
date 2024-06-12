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
      file_content = blob_data.readall().decode('utf-8')

      json_start_indice = [i for i, char in enumerate(file_content) if char == '{']
      json_end_indice = [i for i, char in enumerate(file_content) if char == '}' and i > 0 and file_content[i - 1] != '\\']


      json_list = []
      for start_idx, end_idx in zip(json_start_indice, json_end_indice):
        json_str = file_content[start_idx:end_idx + 1]
        try:
          json_obj = json.loads(json_str)
          json_list.append(json_obj)
        except Exception as e:
          pass

      return jsonify(json_list)
    
    except ResourceNotFoundError as e:
      return f'Error al acceder al archivo: {str(e)}'
    except Exception as e:
      return f'Otro error inesperado: {str(e)}'
    