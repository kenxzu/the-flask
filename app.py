"""WSGI entrypoint for the Flask application."""
from the_flask import create_app

app = create_app()


if __name__ == "__main__":
    app.run()
