from flask import Blueprint, request, jsonify
from services import VehicleService

vehicle_api = Blueprint('vehicle_api', __name__)

@vehicle_api.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.json
    vehicle = VehicleService.create_vehicle(data)
    return jsonify(vehicle), 201

@vehicle_api.route('/vehicles/<string:VIN>', methods=['GET'])
def get_vehicle(VIN):
    vehicle = VehicleService.get_vehicle(VIN)
    return jsonify(vehicle), 200

@vehicle_api.route('/vehicles/<string:VIN>', methods=['PUT'])
def update_vehicle(VIN):
    data = request.json
    vehicle = VehicleService.update_vehicle(VIN, data)
    return jsonify(vehicle), 200

@vehicle_api.route('/vehicles/<string:VIN>', methods=['DELETE'])
def delete_vehicle(VIN):
    VehicleService.delete_vehicle(VIN)
    return jsonify({"message": "Vehicle deleted"}), 204
