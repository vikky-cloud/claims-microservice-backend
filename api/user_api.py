from flask import Blueprint, request, jsonify
from dal.user_dal import UserDAL
from services.user_service import UserService

user_api = Blueprint('user_api', __name__)

@user_api.route('/register', methods=['POST'])
def register():
    data = request.json
    result = UserService.register_user(data['email'], data['password'])  # Call the service layer

    if not result["success"]:
        return jsonify({'message': result["message"]}), 400

    return jsonify({'message': 'User registered successfully'}), 201

@user_api.route('/login', methods=['POST'])
def login():
    data = request.json
    user = UserDAL.get_user_by_email(data['email'])

    if user and user.password == data['password']:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

