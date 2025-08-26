from flask import Blueprint, request, jsonify
from service.plano_estudo_service import PlanoEstudoService


plano_estudo_bp = Blueprint("estudos", __name__)
service = PlanoEstudoService()


@plano_estudo_bp.route("/", methods=["POST"])
def criar():
    dados = request.json
    return jsonify(service.criar(dados, "7SmStkYaBylTaDyFiANr")), 201


@plano_estudo_bp.route("/<string:id>", methods=["PUT"])
def editar(id):
    dados = request.json
    plano = service.listar_por_id(id, "7SmStkYaBylTaDyFiANr")
    if not plano:
        return jsonify({"erro": "Plano de estudo não localizado"}), 404
    
    plano_edit = service.editar(id, "7SmStkYaBylTaDyFiANr", dados)
    return jsonify(plano_edit), 200


@plano_estudo_bp.route("/<string:id>", methods=["GET"])
def listar_por_id(id):
    plano = service.listar_por_id(id, "7SmStkYaBylTaDyFiANr")
    if not plano:
        return jsonify({"erro": "Plano de estudo não localizado"}), 404
    return jsonify(plano), 200


@plano_estudo_bp.route("/", methods=["GET"])
def listar():
    planos = service.listar("7SmStkYaBylTaDyFiANr")
    if not planos:
        return jsonify({"erro": "Nenhum plano de estudo localizado"}), 404
    return jsonify(planos), 200


@plano_estudo_bp.route("/<string:id>", methods=["DELETE"])
def deletar(id):
    plano = service.deletar(id, "7SmStkYaBylTaDyFiANr")
    if not plano:
        return jsonify({"erro": "Plano de estudo não localizado"}), 404
    return ' ', 204

