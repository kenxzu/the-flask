from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_extensions(app):
    """Bind application-wide extensions."""
    db.init_app(app)
