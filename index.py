from flask import Flask, render_template, url_for
from flask_login import LoginManager
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/")
def index():
  return render_template('index.jade', main_css = url_for('static',filename='main.css'))

