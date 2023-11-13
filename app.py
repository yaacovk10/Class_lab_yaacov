from flask import Flask,render_template, request
from tools.numbers.simp import *
from tools.numbers.comp import *
from tools.col import myzip

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", result="")

@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = float(request.form.get('number1'))
    num2 = float(request.form.get('number2'))
    operation = request.form.get('operation')
    print(operation)
    result = perform_operation(num1, num2, operation)
    print(result)
    return render_template("index.html", result=f"Result: {result}")

@app.route("/check", methods=["POST"])
def check():
    num = int(request.form.get('number'))
    print(num)
    operation = request.form.get('operation2')
    print(operation)
    res = action(num,operation)
    print(res)
    return render_template("index.html", res = f"Result: {res}" )



if __name__ == "__main__":
    app.run(debug=True, port=5000)
