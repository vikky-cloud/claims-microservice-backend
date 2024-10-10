from flask import Blueprint, request, jsonify
from services import StatusService

status_api = Blueprint('status_api', __name__)

@status_api.route('/statuses', methods=['POST'])
def create_status():
    data = request.json
    status = StatusService.create_status(data)
    return jsonify(status), 201

@status_api.route('/statuses/<int:status_id>', methods=['GET'])
def get_status(status_id):
    status = StatusService.get_status(status_id)
    return jsonify(status), 200

@status_api.route('/statuses/<int:status_id>', methods=['PUT'])
def update_status(status_id):
    data = request.json
    status = StatusService.update_status(status_id, data)
    return jsonify(status), 200

@status_api.route('/statuses/<int:status_id>', methods=['DELETE'])
def delete_status(status_id):
    StatusService.delete_status(status_id)
    return jsonify({"message": "Status deleted"}), 204
