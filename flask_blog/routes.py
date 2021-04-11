from flask_blog.models import User, Post
from flask import render_template, url_for, flash, redirect
#url_for finds the exact routes for us so that we don't worry about it in main
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog import app

#dummy data as it should be fetched from database
posts = [{
    'author' : 'George RR Martin',
    'title' : 'Winds of Winter Update',
    'content' : 'Don\'t Bother! Read something else please!',
    'date' : '31/03/2021'
},
{
    'author' : 'JK Rowling',
    'title' : 'The Cuckoo\'s Calling',
    'content' : 'Won Something! Again!! Great Day ;)',
    'date' : '29/03/2021'
},
{
    'author' : 'George RR Martin',
    'title' : 'Winds of Winter Update',
    'content' : 'Releasing Soon! I am working as hard as possible!!',
    'date' : '15/03/2021'
}]

@app.route('/')     #Root Page
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home Page',posts = posts)
# The Templating Engine that Flask uses is called is k/a Jinja

@app.route('/about')     #About Page
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET', 'POST'])     #Registration Page
def register():
    form = RegistrationForm()
    #hidden_tag(): Adds Cross Site Request Forgery Token
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}.', 'success')
        return redirect(url_for('home'))     #url_for takes the name of method like home, register, login not html page
    return render_template('register.html', title = 'Signup', form = form)

@app.route('/login', methods = ['GET', 'POST'])     #Login Page
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '12345':
            flash(f'Login Successful.', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Check Username and Password', 'danger')
    return render_template('login.html', title = 'Signin', form = form)