from flask_restful import Resource, reqparse
from models.usuario import UserModel


class Hotel(Resource):
    
    def get(self, user_id):
        user = UserModel.find_user(user_id) 
        if user:
            return user.json()
        return {'message': 'USer not found.'}, 404

    def delete(self, user_id):
         user = UserModel.find_user(user_id)
         if user:
             try:
                 user.delete_hotel()
             except:
                 return {'message': 'An error ocurred trying to delete user.'}, 500
             return{'message': 'User deleted.'}
         return{'message': 'User not found.'}, 404






