from flask import Blueprint

bpMain = Blueprint('main', __name__)

@bpMain.route('/')
def home():
  return 'Hola'