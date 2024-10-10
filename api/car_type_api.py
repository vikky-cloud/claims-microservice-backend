from flask import Blueprint, request, jsonify
from services import CarTypeService

car_type_api = Blueprint('car_type_api', __name__)

@car_type_api.route('/car_types', methods=['POST'])
def create_car_type():
    data = request.json
    car_type = CarTypeService.create_car_type(data)
    return jsonify(car_type), 201

@car_type_api.route('/car_types/<int:car_type_id>', methods=['GET'])
def get_car_type(car_type_id):
    car_type = CarTypeService.get_car_type(car_type_id)
    return jsonify(car_type), 200

@car_type_api.route('/car_types/<int:car_type_id>', methods=['PUT'])
def update_car_type(car_type_id):
    data = request.json
    car_type = CarTypeService.update_car_type(car_type_id, data)
    return jsonify(car_type), 200

@car_type_api.route('/car_types/<int:car_type_id>', methods=['DELETE'])
def delete_car_type(car_type_id):
    CarTypeService.delete_car_type(car_type_id)
    return jsonify({"message": "Car type deleted"}), 204
