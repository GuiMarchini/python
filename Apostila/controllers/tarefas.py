from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import requests
from config import login_obrigatorio
from database import (
    buscar_tarefas_usuario,
    criar_tarefa,
    buscar_tarefa_por_id,
    atualizar_tarefa,
    excluir_tarefa,
    concluir_tarefa,
    buscar_progresso
)

tarefas = Blueprint("tarefas", __name__)


@tarefas.route("/")
def inicio():
    if "usuario_id" in session:
        return redirect(url_for("tarefas.dashboard"))
    return redirect(url_for("auth.login"))


@tarefas.route("/dashboard")
@login_obrigatorio
def dashboard():
    tarefas_lista = buscar_tarefas_usuario(session["usuario_id"])

    frase = "Tenha um ótimo dia e continue avançando!"
    try:
        resposta = requests.get(
            "https://api.adviceslip.com/advice", timeout=3
        )
        if resposta.ok:
            frase = resposta.json()["slip"]["advice"]
    except requests.RequestException:
        pass

    return render_template(
        "dashboard.html",
        tarefas=tarefas_lista,
        frase=frase
    )


@tarefas.route("/nova_tarefa", methods=["GET", "POST"])
@login_obrigatorio
def nova_tarefa():
    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        descricao = request.form["descricao"].strip()
        status = request.form["status"]

        if not titulo:
            flash("O título é obrigatório.")
            return redirect(url_for("tarefas.nova_tarefa"))

        criar_tarefa(titulo, descricao, status, session["usuario_id"])

        flash("Tarefa criada com sucesso!")
        return redirect(url_for("tarefas.dashboard"))

    return render_template("nova_tarefa.html")


@tarefas.route("/editar/<int:id>", methods=["GET", "POST"])
@login_obrigatorio
def editar(id):
    tarefa = buscar_tarefa_por_id(id, session["usuario_id"])

    if not tarefa:
        return "Tarefa não encontrada.", 404

    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        descricao = request.form["descricao"].strip()
        status = request.form["status"]

        if not titulo:
            flash("O título é obrigatório.")
            return redirect(url_for("tarefas.editar", id=id))

        atualizar_tarefa(id, session["usuario_id"], titulo, descricao, status)

        flash("Tarefa atualizada!")
        return redirect(url_for("tarefas.dashboard"))

    return render_template("editar.html", tarefa=tarefa)


@tarefas.route("/excluir/<int:id>")
@login_obrigatorio
def excluir(id):
    excluir_tarefa(id, session["usuario_id"])
    flash("Tarefa excluída.")
    return redirect(url_for("tarefas.dashboard"))


@tarefas.route("/concluir/<int:id>")
@login_obrigatorio
def concluir(id):
    concluir_tarefa(id, session["usuario_id"])
    return redirect(url_for("tarefas.dashboard"))


@tarefas.route("/progresso")
@login_obrigatorio
def progresso():
    dados = buscar_progresso(session["usuario_id"])
    return render_template("progresso.html", dados=dados)