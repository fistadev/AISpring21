from flask import Flask,render_template,request,redirect,url_for,send_from_directory,flash,make_response
from app.constants.items import *
import os
from werkzeug.utils import secure_filename
from app.util.db.connect import db_engine 
from app.util.db.models.project import Project
from app.util.db.models.user import User
from app.util.mail import Mail
from app.util.jwt import generate_token,verify_token
from sqlalchemy.orm import Session
from functools import wraps

engine = db_engine()

session = Session(engine, future=True)

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config["UPLOAD_FOLDER"]="files"


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        ## if token is found in cookies
        token = request.cookies.get("access_token")
        if(token):
            payload = verify_token(token)
            user = session.query(User).get(payload.get("id"))
            user = user.toJSON()
            return f(user, *args, **kws)
        else:
            flash("You need to login to proceed.",'warning')
            return redirect(url_for('login'))           
    return decorated_function


def filterFunction(item,user):
    if item.get("label")=='Dashboard':
        if user:
            return True
        else:
            return False
    else:
        return True

@app.route("/")
def index():
    token = request.cookies.get("access_token")
    user = None
    if(token):
        payload = verify_token(token)
        user = session.query(User).get(payload.get("id"))
        user = user.toJSON()
    all_projects = [project.toJSON() for project in session.query(Project)]
    return render_template('/views/home.html',APP_NAME=APP_NAME,MENU_ITEMS=MENU_ITEMS,SOCIAL_LINKS=SOCIAL_LINKS,all_projects=all_projects,user=user)
 


@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == "GET":
        return render_template('/views/auth/signup.html',APP_NAME=APP_NAME)
    else:
        name = request.form['name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        if name and last_name and email and password:
            user = User(name=name, last_name=last_name, email=email,password_hash=password)
            user.hash_password()
            session.add(user)
            session.commit()
            flash("User is registered!",'success')
            return redirect(url_for('signup'))
        else:
            flash("Invalid parameters!",'danger')
            return redirect(url_for('signup'))

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == "GET":
        return render_template('/views/auth/login.html',APP_NAME=APP_NAME)
    else:
        email = request.form['email']
        password = request.form['password']
        user = session.query(User).where(User.email==email).first()
        if user:
            matching = user.check_password(password)
            if matching:
                print(matching)
                response= make_response(redirect(url_for("dashboard")))
                user = user.toJSON()
                access_token = generate_token(user.get("id"))
                response.set_cookie('access_token',access_token)
                return response
            else:
                flash("Password is not correct!".format(email),"danger")
                return redirect(url_for("login"))
                
        else:
            flash("User with {} is not found !".format(email),"danger")
            return redirect(url_for("login"))

@app.post("/logout")
def logout():
    response = make_response(redirect(url_for("login")))
    response.set_cookie('access_token',expires=0)
    return response;

@app.route("/dashboard")
@authorize
def dashboard(user):
    return  render_template("/views/dashboard/index.html",APP_NAME=APP_NAME,DASHBOARD_MENU=DASHBOARD_MENU,user=user)


@app.route("/dashboard/files",methods=["GET","POST"])
def files():
    if request.method=="POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        return redirect(url_for("files"))
       # FİLE UPLOAD
    else:
        files = os.listdir(os.path.join(app.config["UPLOAD_FOLDER"]))
        return render_template("/views/files/index.html",APP_NAME=APP_NAME,DASHBOARD_MENU=DASHBOARD_MENU,files=files)



@app.route("/dashboard/projects")
def projects():
    all_projects = [project.toJSON() for project in session.query(Project)]
    return render_template("/views/projects/index.html",APP_NAME=APP_NAME,DASHBOARD_MENU=DASHBOARD_MENU,all_projects=all_projects)


@app.route("/dashboard/projects/<string:id>",methods=["GET","POST"])
def project_actions(id):
    if request.method=="POST":
        project_to_delete = session.query(Project).get(int(id))
        session.delete(project_to_delete)
        session.commit()
        return redirect(url_for("projects"))
    else:
        return redirect(url_for("projects"))


@app.route("/dashboard/projects/new",methods=["GET","POST"])
def new_project():
    if request.method=="POST":
        # grab values from form and write into csv file
        title = request.form.get("title")
        description = request.form.get("description")
        cover = request.form.get("cover")
        githubLink = request.form.get("githubLink")
        liveLink = request.form.get("liveLink")
        new_project = Project(title=title, description=description, cover=cover,githubLink=githubLink,liveLink=liveLink)
        session.add(new_project)
        session.commit()
        return redirect(url_for("projects"))
    else:
        # display form for adding project
        return render_template("/views/projects/new.html",APP_NAME=APP_NAME,DASHBOARD_MENU=DASHBOARD_MENU)


@app.route("/dashboard/files/<string:filename>",methods=["GET","POST"])
def file_actions(filename):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"],filename)
    if request.method=="POST":
        os.remove(file_path)
        return redirect(url_for("files"))
    else:
        return send_from_directory(path=app.root_path,directory=app.config["UPLOAD_FOLDER"],filename=filename)

@app.post("/mail")
def send_mail():
    email = request.form.get("email")
    topic = request.form.get("topic")
    message = request.form.get("message")
    mail_client = Mail()
    sent = mail_client.send(email,topic,message)
    if sent:
        flash("Email sent successfully","success")
        return redirect(url_for("index"))
    else:
        flash("Something happened!","danger")
        return redirect(url_for("index"))


