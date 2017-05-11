from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://moltres:sertlom@localhost/moltres_radio'
db = SQLAlchemy(app)

class UserDAO(db.Model):
  __tablename__ = 'users'

  username = db.Column(db.String(), primary_key=True)
  active = db.Column(db.String())
  activationKey = db.Column(db.String())
  password = db.Column(db.String())
  salt = db.Column(db.String())

  def __init__(self, username, active, activationKey, password, salt):
    self.username = username
    self.active = active
    self.activationKey = activationKey
    self.password = password
    self.salt = salt
