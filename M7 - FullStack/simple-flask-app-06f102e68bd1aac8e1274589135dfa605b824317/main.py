from flask import Flask, render_template


app = Flask(__name__)

# APP_NAME = "Ubeyt's Portfolio"

# MENU_ITEMS = ["about", "projects", "dashboard"]


@app.route("/")
def index():
    return render_template('/views/home.html', APP_NAME=APP_NAME, MENU_ITEMS=MENU_ITEMS)


# @app.route("/about")
# def about():
#     return render_template('/about/index.html', APP_NAME=APP_NAME, MENU_ITEMS=MENU_ITEMS)


# @app.route("/projects")
# def projects():
#     return "<h1>Projects</h1>"


# @app.route("/dashboard")
# def backoffice():
#     return "<h1>Dashboard</h1>"


if __name__ == '__main__':
    app.run(debug=True)


# create folder
mkdir myproject
cd myproject
# Virtual Environment
python3 - m venv venv333
. venv333/bin/activate
pip install Flask


pip install pipenv  # (only once)
# create folder
mkdir myproject2
cd myproject2
pipenv install Flask
