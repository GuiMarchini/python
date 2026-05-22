from flask import Flask

app = Flask(__name__)  # inicio o flask


@app.route("/")
def hello():
    return "Hello"


@app.route("/decorator")
def decorator():
    return 'Decorators em Python são funções que modificam ou aprimoram o comportamento de outras funções ou métodos sem alterar seu código-fonte original. Eles permitem adicionar funcionalidades extras, como login, temporização ou controle de acesso, de maneira elegante, reutilizável e com a sintaxe. No Flask, o decorator @app.route é a forma principal de mapear URLs (endereços web) para funções Python específicas (funções de visualização). Ele funciona como uma "capa" sobre a função, informando ao Flask que, quando um usuário acessar um caminho específico, a função logo abaixo deve ser executada para retornar uma resposta.'


if __name__ == "__main__":
    app.run(debug=True)
