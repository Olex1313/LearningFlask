from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/homepage")
def homepage():
    return "<h1> This is my homepage <h1>"

@app.route("/<name>")
def user(name):
    return f'Hello, fellow {name}'

@app.route('/admin')
def admin():
    return redirect(url_for("homepage"))

if __name__ == "__main__":
    app.run()