"""Application factory and setup hooks."""

import os
from typing import Type, Union

from flask import Flask

from config import BaseConfig, config_by_name
from .extensions import init_extensions
from .routes import register_blueprints

ConfigType = Union[str, Type[BaseConfig]]


def create_app(config: ConfigType | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    config_class = _resolve_config(config)
    app.config.from_object(config_class)
    app.config.from_pyfile("config.py", silent=True)

    _ensure_instance_path(app)
    init_extensions(app)
    register_blueprints(app)

    return app


def _resolve_config(config: ConfigType | None) -> Type[BaseConfig]:
    if config is None:
        env_config = os.getenv("FLASK_CONFIG", "DevelopmentConfig")
        return config_by_name.get(env_config, BaseConfig)

    if isinstance(config, str):
        return config_by_name.get(config, BaseConfig)

    if isinstance(config, type) and issubclass(config, BaseConfig):
        return config

    raise TypeError("Config must be a config class or registered name.")


def _ensure_instance_path(app: Flask) -> None:
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass
