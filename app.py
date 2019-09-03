from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
api = Api(app)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

import models
from src.services.UserService import UserService

api.add_resource(UserService, '/')

if __name__ == '__main__':
    manager.run()
    app.run(debug=True)
