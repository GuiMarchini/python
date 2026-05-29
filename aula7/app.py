import requests
from flask import Flask, render_template, request
from calculator import calcular

app = Flask(__name__)

@app.route("/", methods= ['POST'])
def calculator():
    return calcular()

@app.route("/")
def index():
    return render_template('calculator.html', etapas="", resultado="")

if __name__ == '__main__':
    app.run(debug=True)