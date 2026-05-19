from flask import Flask, render_template

app = Flask(__name__)

@app.route('/base')
def alunos():
    lista_alunos = [
        {"nome": "Ana", "idade": 15, "nota": 1},
        {"nome": "Joao", "idade": 16, "nota": 9},
        {"nome": "Gui", "idade": 17, "nota": 3}
    ]
    return render_template('base.html', alunos = lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)
