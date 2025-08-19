from flask import Blueprint, request, jsonify
from service.plano_estudo_service import PlanoEstudoService


plano_estudo_bp = Blueprint("estudos", __name__)
service = PlanoEstudoService()


@plano_estudo_bp.route("/", methods=["POST"])
def criar():
    dados = request.json
    return jsonify(service.criar(dados))
