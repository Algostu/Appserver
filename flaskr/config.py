import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    SECRET_KEY = 'a\xc8@\xcd\xf3*\xcc\xea\xff\xc3X\x12\xb0`\xf5\x1a\x13\x8e6}\x9fk\x14j'
    db = {
    'user'     : 'root',
    'password' : '1234',
    'host'     : '127.0.0.1',
    'port'     : '3306',
    'database' : 'dodam'
    }
    DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

class DevelopmentConfig(Config):
	# uncomment the line below to use postgres
	# SQLALCHEMY_DATABASE_URI = postgres_local_base
	DEBUG = True

class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(Config):
	DEBUG = False

config_by_name = dict(
	dev=DevelopmentConfig,
	test=TestingConfig,
	prod=ProductionConfig
)

key = Config.SECRET_KEY
