from flask import Blueprint, request, jsonify, session
from config import login_obrigatorio
from database import buscar_tarefas_api

api = Blueprint("api", __name__)


@api.route("/api/tarefas")
@login_obrigatorio
def api_tarefas():
    status = request.args.get("status", "Todos")
    tarefas = buscar_tarefas_api(session["usuario_id"], status)
    return jsonify(tarefas)