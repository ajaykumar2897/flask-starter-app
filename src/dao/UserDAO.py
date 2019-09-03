from ..models.CityModel import City
from flask import jsonify
import json
class UserDAO():
    def getUserList():
        city = City.query.all()
        fe_dict = city.__dict__
        del fe_dict['_sa_instance_state']
        return flask.jsonify(fe_dict)
