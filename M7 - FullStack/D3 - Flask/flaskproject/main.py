from flask import Flask, render_template

app = Flask(__name__)

APP_NAME="FistaDev"

MENU_ITEMS= [{"label":"About","link":"#about"},{"label":"Projects","link":"#projects"},{"label":"Backoffice","link":"/backoffice"}]

@app.route("/")
def index():
    return render_template("/layouts/index.html", APP_NAME=APP_NAME, MENU_ITEMS=MENU_ITEMS)

if __name__ == '__main__':
    app.run(debug=True)
