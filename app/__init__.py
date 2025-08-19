from flask import Flask
from routes.plano_estudo_routes import plano_estudo_bp

def create_app():

    app = Flask(__name__)
    app.register_blueprint(blueprint=plano_estudo_bp, url_prefix="/api/estudos")
    return app