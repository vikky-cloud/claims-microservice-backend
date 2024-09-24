from flask import Blueprint, request, jsonify
from dal.user_dal import UserDAL
from services.user_service import UserService
from werkzeug.security import generate_password_hash, check_password_hash

user_api = Blueprint('user_api', __name__)

@user_api.route('/register', methods=['POST'])
def register():
    data = request.json
    
    # Call UserService to handle registration logic
    result = UserService.register_user(data['email'], data['password'])

    if result["success"]:
        user = result["user"]
        return jsonify({'id': user.id, 'email': user.email}), 201  # Return the user info on success
    else:
        return jsonify({"message": result["message"]}), 400  # Handle failure


@user_api.route('/login', methods=['POST'])
def login():
    data = request.json
    user = UserDAL.get_user_by_email(data['email'])  # Make sure this method fetches the user correctly

    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
    else:
        return jsonify({'error': 'Invalid credentials. Please try again.'}), 401
