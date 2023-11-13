from flask import Flask,render_template, request, session
from tools.numbers.simp import *
from tools.numbers.comp import *
from tools.col import myzip

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Disable Secure and HttpOnly flags for session cookies during development
if app.debug:
    app.config.update(
        SESSION_COOKIE_SECURE=False,
        SESSION_COOKIE_HTTPONLY=False
    )


@app.route("/")
def index():
    # Reset the calculate_called flag to False on each page refresh
    session['calculate_called'] = False
    return render_template("index.html", result="")

@app.route("/calculate", methods=["POST"])
def calculate():
    """
    Choose the function selected by user from simp.py and returns results
    """
    num1 = float(request.form.get('number1'))
    num2 = float(request.form.get('number2'))
    operation = request.form.get('operation')
    result = perform_operation(num1, num2, operation)
     # Set session variable to indicate /calculate has been called
    session['calculate_called'] = True
    return render_template("index.html", result=f"Result: {result}", check_enabled=True)

@app.route("/check", methods=["POST"])
def check():
    """
    Choose the function selected by user from comp.py and returns results
    """
    try:
        # Check if /calculate has been called
        if not session.get('calculate_called', False):
            raise Exception("Please perform /calculate first.")

        num = int(request.form.get('number'))
        operation = request.form.get('operation2')

        # Check if num is an integer
        if not isinstance(num, int):
            raise ValueError("Input must be an integer.")

        res = action(num, operation)

        return render_template("index.html", res=f"Result: {res}", check_enabled=True)

    except Exception as e:
        return render_template("index.html", res=f"Error: {str(e)}", check_enabled=False)

@app.route("/zip", methods=["POST"])
def zip_iterables():
    try:
        iter1 = request.form.get('iter1').split(',')
        iter2 = request.form.get('iter2').split(',')

        # Call the myzip function
        result = myzip(iter1, iter2)

        return render_template("index.html", zip_result=f"Zip Result: {result}")

    except Exception as e:
        return render_template("index.html", zip_result=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
