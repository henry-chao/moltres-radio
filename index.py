from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'superdupersecret'
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://moltres:sertlom@localhost/moltres_radio'
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

from moltresUser import User, UserDAO
import bcrypt

@login_manager.user_loader
def load_user(username):
  return User(username)

@app.route("/")
def index():
  return render_template('index.jade',
    title = "Moltres Radio"
  )

@app.route("/login")
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  return render_template('login.jade',
    title = "Moltres Radio - Login"
  )

@app.route("/register")
def register():
  return render_template('register.jade',
    title = "Moltres Radio - Register",
    validatejs = True
  )

@app.route("/registerSuccess")
def registerSuccess():
  return render_template('register_success.jade',
    title = "Moltres Radio - Register Success"
  )

@app.route("/auth", methods=['POST'])
def auth():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')

    dbAcct =  UserDAO.query.filter_by(username=username).first()
    hashPass = bcrypt.hashpw(password, dbAcct.salt)
  
    if hashPass == dbAcct.password:
      login_user(User(username))
      return redirect(url_for('index'))
    else:
      return redirect(url_for('login'))

@app.route("/register_auth", methods=['POST'])
def register_auth():
  username = request.form.get('username')
  password = request.form.get('password')
  salt = bcrypt.gensalt()
  password = bcrypt.hashpw(password, salt)
  newUser = UserDAO(username, "Y", bcrypt.gensalt(), password, salt)
  db.session.add(newUser)
  db.session.commit()
  return redirect(url_for('registerSuccess'))

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('index'))
