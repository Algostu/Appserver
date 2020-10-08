# python basic library
import os

# external package
from flask import Flask
from sqlalchemy import create_engine, text

## __init__ files:
## 1. bycrypt 실행 하기 : hash 코드 생성하기
## 2. create_app 함수와 같은 클래스, 함수 같은 것들 만들어 놓기
## 3. 임포트 제한 (X)



def create_app(config_name):
    """flask application factory
    args:
        config_name = configuration mode
    """
    # import configuration file
    from . import config
    from .view import api_urls
    from .model import db
    from .extensions import flask_bcrypt, login_manager, sess

    # create and configure the app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_object(config.config_by_name[config_name])

    # apply url
    for url in api_urls:
        app.register_blueprint(url)

    # apply db
    db.init_app(app)
    app.db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

    # apply redis session interface
    sess.init_app(app)

    # apply crypto method
    flask_bcrypt.init_app(app)

    return app
