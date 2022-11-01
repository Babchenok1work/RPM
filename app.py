from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user
from flask_security import Security, login_required, \
     SQLAlchemySessionUserDatastore
from Forms import LoginForm,RegisterForm
from database import db_session, init_db
from models import *
from flask_security import Security, login_required, \
     SQLAlchemySessionUserDatastore
app = Flask(__name__)
app.config['SECURITY_PASSWORD_SALT'] = 'some arbitrary super secret string'
app.config['SECRET_KEY'] = '123aaaasdasdasd'

# Create database connection object
db = SQLAlchemy(app)

user_datastore = SQLAlchemySessionUserDatastore(db_session,
                                                User, Role)
security = Security(app, user_datastore)


@app.route("/home")
@app.route("/")
def index():
    return render_template("index.html",name="alexander")

@app.route("/index1")
def index1():
    return "hello"

@app.route("/user/<string:name>/<int:id>")
def user(name,id):
    return "user name"+name+"user_id"+str(id)


@app.route("/about")
def about():
    return "about page"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(user)
        username = form.username.data
        password = form.password.data
        return redirect('/home')
    return render_template('login.html', title='Sign In', form=form)


@app.before_first_request
def create_user():
    init_db()


@app.route('/signup', methods=['GET', 'POST'])
def Signup():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        username = form.username.data
        user_datastore.create_user(email=email,username=username, password=password)
        db_session.commit()
        return redirect('/home')
    return render_template('Signup.html', title='Sign Up', form=form)

if __name__ == "__main__":
    app.run(debug = True)
