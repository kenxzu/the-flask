"""Blueprint registration helpers."""
from flask import Flask

from .main import bp as main_bp


BLUEPRINTS = (main_bp,)


def register_blueprints(app: Flask) -> None:
    """Register all blueprints with the application."""
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
