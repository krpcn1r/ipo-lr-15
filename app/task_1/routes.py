from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Привет"


@app.route("/hello/<name>")
def hello_user(name):
    return f"Привет: {name}"


@app.route("/square/<int:number>")
def num_square(number):
    return f"Квадрат числа {number}: {str(number * number)}"


@app.route("/length/<text>")
def text_length(text):
    return f"Длина строки '{text}': {len(text)}"


@app.route("/reverse", methods=['POST'])
def reverse_text():
    data = request.data.decode('utf-8')
    return data[::-1]
