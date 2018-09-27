from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from .home import home as home_blueprint
    from .admin import admin as admin_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app