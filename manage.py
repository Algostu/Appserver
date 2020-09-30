#-*-coding:utf-8-*-
import os, sys, json, unittest, time

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Command, Server

from main import create_app
from main.model import db

app = create_app('dev')
app.app_context().push()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host='0.0.0.0', port=5000))

@manager.command
def run():
	app.run()

if __name__ == '__main__':
    manager.run()
