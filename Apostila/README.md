# Painel de Controle de Tarefas - Flask

Projeto simples feito para a atividade de Python/Flask.

## Recursos
- Flask com templates
- SQLite
- Cadastro, login e logout
- Senha protegida com hash
- CRUD de tarefas
- API externa de frase motivacional
- Bootstrap 5
- Filtro de tarefas sem recarregar a página
- Modo escuro salvo no localStorage
- Gráfico de progresso com Chart.js
- Rota REST `/api/tarefas`

## Como executar

No terminal do VS Code, dentro da pasta do projeto:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Depois:

```bash
pip install -r requirements.txt
python app.py
```

Abra no navegador:

```text
http://127.0.0.1:5000
```

O arquivo `tarefas.db` será criado automaticamente na primeira execução.

## Observação

A `SECRET_KEY` está simples apenas para fins didáticos. Em um projeto real, ela deve ser trocada por uma chave secreta.
