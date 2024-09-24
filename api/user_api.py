from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_api = Blueprint('user_api', __name__)

@user_api.route('/register', methods=['POST'])
def register():
    data = request.json
    user = UserService.register_user(data['email'], data['password'])
    return jsonify({'id': user.id, 'email': user.email}), 201

@user_api.route('/login', methods=['POST'])
def login():
    data = request.json
    user = UserService.authenticate_user(data['email'], data['password'])
    if user:
        return jsonify({'id': user.id, 'email': user.email}), 200
    return jsonify({'message': 'Invalid credentials'}), 401
