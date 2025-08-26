from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from service.plano_estudo_service import PlanoEstudoService


plano_estudo_bp = Blueprint("estudos", __name__)
service = PlanoEstudoService()


@plano_estudo_bp.route("/", methods=["POST"])
@jwt_required()
def criar():
    usuario_logado = get_jwt_identity()
    dados = request.json
    return jsonify(service.criar(dados, usuario_logado)), 201


@plano_estudo_bp.route("/<string:id>", methods=["PUT"])
@jwt_required()
def editar(id):
    usuario_logado = get_jwt_identity()
    dados = request.json
    plano = service.listar_por_id(id, usuario_logado)
    if not plano:
        return jsonify({"erro": "Plano de estudo não localizado"}), 404
    
    plano_edit = service.editar(id, usuario_logado, dados)
    return jsonify(plano_edit), 200


@plano_estudo_bp.route("/<string:id>", methods=["GET"])
@jwt_required()
def listar_por_id(id):
    usuario_logado = get_jwt_identity()
    plano = service.listar_por_id(id, usuario_logado)
    if not plano:
        return jsonify({"erro": "Plano de estudo não localizado"}), 404
    return jsonify(plano), 200


@plano_estudo_bp.route("/", methods=["GET"])
@jwt_required()
def listar():
    usuario_logado = get_jwt_identity()
    planos = service.listar(usuario_logado)
    if not planos:
        return jsonify({"erro": "Nenhum plano de estudo localizado"}), 404
    return jsonify(planos), 200


@plano_estudo_bp.route("/<string:id>", methods=["DELETE"])
@jwt_required()
def deletar(id):
    usuario_logado = get_jwt_identity()
    plano = service.deletar(id, usuario_logado)
    if not plano:
        return jsonify({"erro": "Plano de estudo não localizado"}), 404
    return ' ', 204

