from flask_restful import Resource
from ..dao.UserDAO import UserDAO

class UserService(Resource):
    @staticmethod
    def get():
        return UserDAO.getUserList()
