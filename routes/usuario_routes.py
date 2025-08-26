from flask import Blueprint, request, jsonify
from service.usuario_service import UsuarioService

usuario_bp = Blueprint("usuarios", __name__)
service = UsuarioService()


@usuario_bp.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.json
    usuario = service.criar(dados)
    if not usuario:
        return jsonify({"erro": "E-mail já cadastrado!"}), 409
    return jsonify(usuario), 201