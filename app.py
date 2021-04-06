import sqlite3
from flask import Flask, request, render_template, redirect

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


# @app.route("/login", methods=["GET"])
# def login_get():
    # if "user_id" in session:
    # return render_template("login.html")
    # else:  # ログインに飛ばす
    # return redirect('/login')


@app.route("/kifu", methods=["POST"])
def kifu_post():
    # 入力ホーム
    name = request.form.get("name")
    address = request.form.get("address")
    email = request.form.get("email")
    remark = request.form.get("remark")
    conn = sqlite3.connect("Hugtest.db")
    c = conn.cursor()
    c.execute
    ("insert into users values(null,?,?,?,?)", (name, address, email, remark))
    conn.commit()
    conn.close()
    return "ok"
    # return redirect("/2page_not_found.html")  # 関数を飛ばしたい時リダイレクトを


# @app.route('/page_not_found', methods=["GET",])
# def page_not_found():
    # return render_template('/page_not_found.html')

if __name__ == "__main__":
    app.run(debug=True)
