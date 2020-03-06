from app import app
from flask import render_template,flash,redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "miguel"}
    posts = [
        {
            'author':{'username':"john"},
            'body': 'beautful day in portlande!'
        },
        {
            "author":{'username':'susan'},
            'body':'the avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("login requested for user {},remember_me={}".format(
            form.username.data,form.remember_me.data
        ))
        return redirect('index')
    return render_template('login.html',title="sign in",form=form)
