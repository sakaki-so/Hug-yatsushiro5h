import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/login', methods=["GET"])
def login():
    return render_template('login.html')


@app.route('/kifu', methods=["GET"])
def kifu():
    return render_template('kifu.html')


@app.route('/page_not_found', methods=["GET", "POST"])
def page_not_found():
    return render_template('/page_not_found.html')


if __name__ == "__main__":
    app.run(debug=True)
