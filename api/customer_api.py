from flask import Blueprint, request, jsonify
from services import CustomerService

customer_api = Blueprint('customer_api', __name__)

@customer_api.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    customer = CustomerService.create_customer(data)
    return jsonify(customer), 201

@customer_api.route('/customers/<int:customer_number>', methods=['GET'])
def get_customer(customer_number):
    customer = CustomerService.get_customer(customer_number)
    return jsonify(customer), 200

@customer_api.route('/customers/<int:customer_number>', methods=['PUT'])
def update_customer(customer_number):
    data = request.json
    customer = CustomerService.update_customer(customer_number, data)
    return jsonify(customer), 200

@customer_api.route('/customers/<int:customer_number>', methods=['DELETE'])
def delete_customer(customer_number):
    CustomerService.delete_customer(customer_number)
    return jsonify({"message": "Customer deleted"}), 204
