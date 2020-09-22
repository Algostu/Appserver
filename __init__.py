# from flask import Flask
# from flask_bcrypt import Bcrypt
# from sqlalchemy import create_engine, text
#
# from .config import config_by_name
#
# flask_bcrypt = Bcrypt()
#
# def create_app(config_name):
# 	app = Flask(__name__)
#
#     # 설정 로드
# 	app.config.from_object(config_by_name[config_name])
#     database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
#     app.db = database
#
#     # 암호화? 나도 잘은 모르겠다
# 	flask_bcrypt.init_app(app)
#
#
# 	return app
