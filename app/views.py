from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', user = user, title = 'Home', posts = posts)

@app.route('/page')
def page():
    return render_template('page.html')
