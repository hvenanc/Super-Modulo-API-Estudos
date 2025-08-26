from flask import Flask
from flask_cors import CORS
from routes.plano_estudo_routes import plano_estudo_bp
from routes.usuario_routes import usuario_bp

def create_app():

    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}}) #Mantém o CORS Público
    app.register_blueprint(blueprint=plano_estudo_bp, url_prefix="/api/estudos")
    app.register_blueprint(blueprint=usuario_bp, url_prefix="/api/usuarios")
    return app