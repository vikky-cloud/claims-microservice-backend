from flask import Blueprint, request, jsonify
from services import ClaimService

claim_api = Blueprint('claim_api', __name__)

@claim_api.route('/claims', methods=['POST'])
def create_claim():
    data = request.json
    claim = ClaimService.create_claim(data)
    return jsonify(claim), 201

@claim_api.route('/claims/<int:claim_number>', methods=['GET'])
def get_claim(claim_number):
    claim = ClaimService.get_claim(claim_number)
    return jsonify(claim), 200

@claim_api.route('/claims/<int:claim_number>', methods=['PUT'])
def update_claim(claim_number):
    data = request.json
    claim = ClaimService.update_claim(claim_number, data)
    return jsonify(claim), 200

@claim_api.route('/claims/<int:claim_number>', methods=['DELETE'])
def delete_claim(claim_number):
    ClaimService.delete_claim(claim_number)
    return jsonify({"message": "Claim deleted"}), 204
