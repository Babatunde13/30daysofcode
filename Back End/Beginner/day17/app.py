from flask import Flask, render_template
import json

app = Flask(__name__)


def save_file(add):
    with open('forms.txt', 'a') as f:
        f.write(add)
        
def deleted():
    with open('forms.txt', 'r+') as f:
        f.truncate(0)

@app.route('/')
def home():
    return 'Hello From Flask!'

@app.route('/add/<newword>/')
def word(newword):
    save_file('\n'+newword)
    return f'<h3>{newword} added to file successfully</h3>'

@app.route('/list/')
def list():
    with open('forms.txt', 'r') as f:
        data = [l for l in f.readlines()]
    
    return render_template('list.html', words=data)

@app.route('/delete/')
def delete():
    deleted()
    return '<h3>Successfully deleted file content</h3>'


if __name__ == "__main__":
    app.run()