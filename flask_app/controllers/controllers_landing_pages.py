from flask_app import app
from flask import render_template,redirect
# from flask_app.models.models_user import user
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/rc')
def rc():
    return render_template('rc.html')

