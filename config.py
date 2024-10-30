import os

class Config:
    SECRET_KEY = os.urandom(24)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'db', 'app.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False