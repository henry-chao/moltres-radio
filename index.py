from flask import Flask, render_template
from flask_login import LoginManager
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/")
def index():
  return render_template('index.jade')

