from models.policy import Policy
from app import db

class PolicyDAL:

    @staticmethod
    def create_policy(data):
        new_policy = Policy(
            policy_number=data['policy_number'],
            policy_limit=data['policy_limit'],
            deductible=data['deductible'],
            expiration_date=data['expiration_date'],
            customer_number=data['customer_number'],
            VIN=data['VIN']
        )
        db.session.add(new_policy)
        db.session.commit()
        return new_policy

    @staticmethod
    def get_policy_by_number(policy_number):
        return Policy.query.get(policy_number)

    @staticmethod
    def update_policy(policy_number, data):
        policy = Policy.query.get(policy_number)
        if policy:
            policy.policy_limit = data.get('policy_limit', policy.policy_limit)
            policy.deductible = data.get('deductible', policy.deductible)
            policy.expiration_date = data.get('expiration_date', policy.expiration_date)
            policy.customer_number = data.get('customer_number', policy.customer_number)
            policy.VIN = data.get('VIN', policy.VIN)
            db.session.commit()
        return policy

    @staticmethod
    def delete_policy(policy_number):
        policy = Policy.query.get(policy_number)
        if policy:
            db.session.delete(policy)
            db.session.commit()
        return policy
