from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<info>")
def homepage(info):
    return render_template('index.html', content = info, r = 2)

@app.route('/admin')
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()