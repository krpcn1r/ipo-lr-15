from app.task_1.routes import app, Routes

name = input("Введите имя: ")
num = int(input("Введите числo: "))
text = input("Введите строку: ")

route_data = Routes(name, num, text)

app.run(debug=True)
