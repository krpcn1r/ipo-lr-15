from flask import Flask

app = Flask(__name__)

route_instance = None


class Routes:
    def __init__(self, name, num, text):
        self.name = name
        self.num = num
        self.text = text


@app.route("/")
def hello():
    return "Hello!"


@app.route("/hello/<name>")
def hello_user(name):
    if route_instance and route_instance.name:
        return f"Привет {route_instance.name}"
    return f"Привет {name}"


@app.route("/square/<int:number>")
def num_square(number):
    return str(number * number)


@app.route("/text")
def show_text():
    if route_instance:
        return f"Текст из конструктора: {route_instance.text}"
    return "Данные не инициализированы"


if __name__ == '__main__':
    name = input("Введите имя: ")
    num = int(input("Введите число: "))
    text = input("Введите строку: ")

    route_instance = Routes(name, num, text)

    app.run(debug=True)