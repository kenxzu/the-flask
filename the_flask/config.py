"""Configuration objects for the Flask application."""
import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://username:password@localhost/flaskdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "a-temporary-key-for-development")
