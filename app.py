from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from Forms import LoginForm
from models import db
app = Flask(__name__)
app.config['SECRET_KEY'] = '123aaaasdasdasd'

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
        username = form.username.data
        password = form.password.data
        print(username,password)
        return redirect('/home')
    return render_template('login.html', title='Sign In', form=form)

if __name__ == "__main__":
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug = True)
