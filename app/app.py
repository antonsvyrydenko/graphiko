#!/usr/bin/env python
# coding: utf-8
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config


db = SQLAlchemy()


def create_api_app(config_name: str) -> Flask:

    app = Flask(__name__)
    CORS(app)
    app = Config().get_config(app, config_name)

    db.init_app(app)

    from .api import api_bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api/1.0")

    return app
