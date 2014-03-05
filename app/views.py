from app import app, db
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

