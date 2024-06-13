from flask import Flask
from flask_cors import CORS
from config import config

from routes.routeMain import bpMain

app = Flask(__name__)
CORS(app)
app.register_blueprint(bpMain)

if __name__ == '__main__':
  app.config.from_object(config['development'])
  app.run()