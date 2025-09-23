from flask import Flask
from config import Config
from extension import db
from model import Message




app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

        
from routes.main_routes import main

app.register_blueprint(main)
