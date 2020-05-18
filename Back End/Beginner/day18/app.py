from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask.'

@app.route('/best-movie/')
def best():
    return render_template('best-movie.html', best='Jumanji: The Next Level')

if __name__ == "__main__":
    app.run()