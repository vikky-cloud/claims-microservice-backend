from flask import Blueprint, request, jsonify
from services import AddressService

address_api = Blueprint('address_api', __name__)

@address_api.route('/addresses', methods=['POST'])
def create_address():
    data = request.json
    address = AddressService.create_address(data)
    return jsonify(address), 201

@address_api.route('/addresses/<string:zipcode>', methods=['GET'])
def get_address(zipcode):
    address = AddressService.get_address(zipcode)
    return jsonify(address), 200

@address_api.route('/addresses/<string:zipcode>', methods=['PUT'])
def update_address(zipcode):
    data = request.json
    address = AddressService.update_address(zipcode, data)
    return jsonify(address), 200

@address_api.route('/addresses/<string:zipcode>', methods=['DELETE'])
def delete_address(zipcode):
    AddressService.delete_address(zipcode)
    return jsonify({"message": "Address deleted"}), 204
