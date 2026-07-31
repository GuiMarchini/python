from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from config import login_obrigatorio
from database import criar_usuario, verificar_login

auth = Blueprint("auth", __name__)


@auth.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"].strip()
        email = request.form["email"].strip().lower()
        senha = request.form["senha"]

        if not nome or not email or not senha:
            flash("Preencha todos os campos.")
            return redirect(url_for("auth.registro"))

        if not criar_usuario(nome, email, senha):
            flash("Este e-mail já está cadastrado.")
            return redirect(url_for("auth.registro"))

        flash("Cadastro realizado! Agora faça login.")
        return redirect(url_for("auth.login"))

    return render_template("registro.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        senha = request.form["senha"]

        usuario = verificar_login(email, senha)

        if usuario:
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]
            return redirect(url_for("tarefas.dashboard"))

        flash("E-mail ou senha incorretos.")

    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))