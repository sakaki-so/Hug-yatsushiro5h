import sqlite3
from flask import Flask, render_template  # listを表示

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route("/base.html")
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
