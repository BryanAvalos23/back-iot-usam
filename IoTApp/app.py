from flask import Flask
import os
from flask_cors import CORS
from dotenv import load_dotenv

from config import config
from routes.routeMain import bpMain

load_dotenv()

port = int(os.getenv('PORT', 5000))
host = os.getenv('HOST', '0.0.0.0')

app = Flask(__name__)
CORS(app)
app.register_blueprint(bpMain)

if __name__ == '__main__':
  app.config.from_object(config['development'])
  app.run(host=host, port=port)