from flask import Flask, request

app = Flask(__name__)

# Обработчик корневой страницы
@app.route("/")
def hello():
    return "Привет"

# Маршрут для приветствия пользователя 
@app.route("/hello/<name>")
def hello_user(name):
    return f"Привет: {name}"

# Маршрут для возведения числа в квадрат
@app.route("/square/<int:number>")
def num_square(number):
    return f"Квадрат числа {number}: {str(number * number)}"

# Маршрут для вычисления длины переданной строки
@app.route("/length/<text>")
def text_length(text):
    return f"Длина строки '{text}': {len(text)}"

# Обработчик POST-запроса, который переворачивает текст
@app.route("/reverse", methods=['POST'])
def reverse_text():
    data = request.data.decode('utf-8')
    # Возврат перевернутой строки 
    return data[::-1]
