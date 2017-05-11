from index import *

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

  def __repr__(self):
    return '<User %r>' % self.username

class User:
  username = ""

  def __init__(self, username):
    self.username = username

  @property
  def is_active(self):
    #dbUser = UserDAO.query.filter(username=self.username).first()
    #return dbUser.active
    return True

  @property
  def is_authenticated(self):
    return True

  @property
  def is_anonymous(self):
    return False

  def get_id(self):
    return self.username

