from flask import Blueprint
from services.serviceExtractData import AccessDataFromAzure

bpMain = Blueprint('main', __name__)

@bpMain.route('/')
def home():
  namefile = '0_1646ffdf6233459eb6b2b039ac1375d2_1.json'
  message = AccessDataFromAzure.access_data(namefile)
  print(message)
  return 'check the console'