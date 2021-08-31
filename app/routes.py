from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import os


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    path = 'static/Legos'
    list_of_files = []

    for root, dirs, files in os.walk('./app/static/Legos'):
	    for file in files:
		    list_of_files.append(os.path.join(path,file))
    # for name in list_of_files:
    #     print(name)

    return render_template('index.html', title='Home', user=user, posts=posts, images = list_of_files)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)


@app.route('/<item>', methods=['GET'])
def show(item):
    path = 'static/Legos'
    image = os.path.join(path,item)
    return render_template('showimage.html',image = image)


@app.route('/minecraft')
def minecraft():
    
    path = 'static/Legos'
    list_of_files = []

    for root, dirs, files in os.walk('./app/static/Legos'):
	    for file in files:
		    list_of_files.append(os.path.join(path,file))
    # for name in list_of_files:
    #     print(name)

    return render_template('index.html', title='Home', images = list_of_files)

    