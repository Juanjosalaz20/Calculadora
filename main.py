from flask import Flask, request, render_template
from operaciones import sumar, restar, multiplicar, dividir, random_1
from livereload import Server

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/suma")
def ruta_suma():
    num1=request.args.get('num1',type=float)
    num2=request.args.get('num2',type=float)
    if num1 is None or num2 is None:
        return 'Faltan datos'

    return f'la suma de num1 y num2 es {sumar(num1, num2)}'

@app.route("/resta")
def ruta_resta():
    num1=request.args.get('num1',type=float)
    num2=request.args.get('num2',type=float)
    if num1 is None or num2 is None:
        return 'Faltan datos'

    return f'la resta de num1 y num2 es {restar(num1, num2)}'

@app.route("/multiplicacion")
def ruta_multiplicacion():
    num1=request.args.get('num1',type=float)
    num2=request.args.get('num2',type=float)
    if num1 is None or num2 is None:
        return 'Faltan datos'

    return f'la multiplicacion de num1 y num2 es {multiplicar(num1, num2)}'

@app.route("/division")
def ruta_division():
    num1=request.args.get('num1',type=float)
    num2=request.args.get('num2',type=float)
    if num1 is None or num2 is None:
        return 'Faltan datos'

    return f'la division de num1 y num2 es {dividir(num1, num2)}'

@app.route("/aleatorio")
def ruta_aleatorio():
    num1=request.args.get('num1',type=float)
    num2=request.args.get('num2',type=float)
    if num1 is None or num2 is None:
        return 'Faltan datos'

    return f'el numero aleatorio entre num1 y num2 es {random_1(num1, num2)}'

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
