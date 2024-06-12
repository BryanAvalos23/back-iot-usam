from flask import Flask
from config import config

from routes.routeMain import bpMain

app = Flask(__name__)
app.register_blueprint(bpMain)

if __name__ == '__main__':
  app.config.from_object(config['development'])
  app.run()