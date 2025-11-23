"""
Archivo principal de la aplicación Flask
Desarrollado por Lina Chamorro — IP3-Taller1
"""

import os
from flask import Flask
from flask_restful import Api
from flasgger import Swagger  
from models import db
from resources.video import Video
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    api = Api(app)
    swagger = Swagger(app) 

    api.add_resource(Video, "/api/videos/<int:video_id>")

    return app

if __name__ == "__main__":
    config_name = os.getenv('FLASK_CONFIG', 'development')
    app = create_app(config_name)

    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000)
