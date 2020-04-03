from flask import Flask, render_template, redirect, url_for, flash
from app import app
from app.forms import LoginForm

@app.route('/home')
@app.route('/')  #'http://www.google.com/'
def home():
	user = {'username': 'Masum'}
	
	posts = [
		{
			'author' : {'username': 'John'},
			'body': 'This is a beautiful day!'
		},
		{
			'author' : {'username': 'Bob'},
			'body': "I'm good today!"
		},
		{
			'author' : {'username': 'Alice'},
			'body': 'got a new job today.'
		}
		
		
	]
		
	return render_template('home.html', title='Home', user=user, posts=posts)
	
@app.route('/product')  #'http://www.google.com/'
def product():
	return render_template('product.html')
	
@app.route('/about') 
def about():
	return render_template('about.html')
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for the user {}'.format(form.username.data))
		
		return redirect(url_for('home'))
	
	return render_template('login.html', title='Sign In Here', form=form)
	
	
	
	
	
	