import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-temporary-key-for-development'