from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from moltresUser import User
app = Flask(__name__)
app.secret_key = 'superdupersecret'
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
  return User(username)

@app.route("/")
def index():
  return render_template('index.jade', main_css = url_for('static',filename='main.css'))

@app.route("/login")
def login():
  return render_template('login.jade', main_css = url_for('static',filename='main.css'))

@app.route("/auth", methods=['POST'])
def auth():
  if request.method == 'POST':
    user = User(request.form.get('username'))
    if login_user(user):
      return redirect(url_for('index'))
    else:
      return redirect(url_for('login'))

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('index'))
