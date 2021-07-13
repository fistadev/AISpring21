from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/goodreads')
def goodreads():
    return render_template('goodreads.html')


if __name__ == "__main__":
    app.run(debug=True)
