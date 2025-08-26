from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from routes.plano_estudo_routes import plano_estudo_bp
from routes.usuario_routes import usuario_bp

jwt = JWTManager()

def create_app():

    app = Flask(__name__)
    load_dotenv()

    #JWT
     # Configurações do JWT
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_API")
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_HEADER_NAME"] = "Authorization"
    app.config["JWT_HEADER_TYPE"] = "Bearer"
    jwt.init_app(app)

    #CORS

    CORS(app, resources={r"/api/*": {"origins": "*"}}) #Mantém o CORS Público
    app.register_blueprint(blueprint=plano_estudo_bp, url_prefix="/api/estudos")
    app.register_blueprint(blueprint=usuario_bp, url_prefix="/api/usuarios")
    return app