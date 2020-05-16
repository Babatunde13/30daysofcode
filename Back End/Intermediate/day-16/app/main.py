from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')
    