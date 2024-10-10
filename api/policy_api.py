from flask import Blueprint, request, jsonify
from services import PolicyService

policy_api = Blueprint('policy_api', __name__)

@policy_api.route('/policies', methods=['POST'])
def create_policy():
    data = request.json
    policy = PolicyService.create_policy(data)
    return jsonify(policy), 201

@policy_api.route('/policies/<string:policy_number>', methods=['GET'])
def get_policy(policy_number):
    policy = PolicyService.get_policy(policy_number)
    return jsonify(policy), 200

@policy_api.route('/policies/<string:policy_number>', methods=['PUT'])
def update_policy(policy_number):
    data = request.json
    policy = PolicyService.update_policy(policy_number, data)
    return jsonify(policy), 200

@policy_api.route('/policies/<string:policy_number>', methods=['DELETE'])
def delete_policy(policy_number):
    PolicyService.delete_policy(policy_number)
    return jsonify({"message": "Policy deleted"}), 204
