from models.claim import Claim
from app import db

class ClaimDAL:

    @staticmethod
    def create_claim(data):
        new_claim = Claim(
            amount=data['amount'],
            claim_date=data['claim_date'],
            policy_number=data['policy_number'],
            status_id=data['status_id']
        )
        db.session.add(new_claim)
        db.session.commit()
        return new_claim

    @staticmethod
    def get_claim_by_id(claim_number):
        return Claim.query.get(claim_number)

    @staticmethod
    def update_claim(claim_number, data):
        claim = Claim.query.get(claim_number)
        if claim:
            claim.amount = data.get('amount', claim.amount)
            claim.claim_date = data.get('claim_date', claim.claim_date)
            claim.policy_number = data.get('policy_number', claim.policy_number)
            claim.status_id = data.get('status_id', claim.status_id)
            db.session.commit()
        return claim

    @staticmethod
    def delete_claim(claim_number):
        claim = Claim.query.get(claim_number)
        if claim:
            db.session.delete(claim)
            db.session.commit()
        return claim
