"""Application factory for the Flask project."""
from flask import Flask

from .config import Config
from .extensions import db
from .blueprints import register_blueprints


def create_app(config_object: type[Config] = Config) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask) -> None:
    """Bind extensions to the application instance."""
    db.init_app(app)

__all__ = ["create_app"]
