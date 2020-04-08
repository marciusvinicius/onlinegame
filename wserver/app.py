from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_restplus import Api
from flask import Blueprint

from auth.resource import api as user_ns

from config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )
api.add_namespace(user_ns, path='/user')

def create_app(config_name):
    app = Flask(__name__)
    #Migrate this to environ
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    return app
