from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Guilherme Marchini</li>  
                <li><strong>Email:</strong> 12400181@cotemig.com.br</li>
                <li><strong>Telefone:</strong> (31) 9632-6525</li>
                <li><strong>Endereço:</strong> Coração Eucarístico</li> 
            </ul>

            <h2>Experiência Profissional</h2>
            <ul>
                <li><strong>Empresa:</strong> Microsoft</li>
                <li><strong>Cargo:</strong> Desenvolvedor de Software</li>
                <li><strong>Período:</strong> Jan 2020 - Presente</li>
            </ul>

            <h2>Educação</h2>
            <ul>
                <li><strong>Escola:</strong> Colégio Cotemig</li>  
                <li><strong>Curso:</strong> Desenvolvimento Web e Mobile</li>
                <li><strong>Tempo:</strong> 2024 - ATUAL</li>
            </ul>
        </body>
        </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
