from flask import Flask
from config import SECRET_KEY, criar_banco
from controllers import auth, tarefas, api

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(auth)
app.register_blueprint(tarefas)
app.register_blueprint(api)


if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)