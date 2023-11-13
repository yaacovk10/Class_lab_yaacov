from flask import Flask,render_template
from tools.numbers.simp import *
from tools.numbers.comp import *
from tools.col import myzip

app = Flask(__name__)


@app.route("/")
def index():
    print(f"adding : {adding(2,3)}")
    print(f"substracting : {substracting(3,2)}")
    print(f"sum of digits :{sumofdigits(32)}")
    print(f"is palindrome : {is_palindrome(232)}")
    print(f"zip of [1,2,3] and ['one', 'two','three']: {myzip([1,2,3], ['one', 'two','three'])}")
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True, port=7000)
