"""WSGI entrypoint for production servers."""

from app import create_app

app = create_app("ProductionConfig")
