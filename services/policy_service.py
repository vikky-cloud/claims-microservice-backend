from dal.policy_dal import PolicyDAL

class PolicyService:

    @staticmethod
    def create_policy(data):
        return PolicyDAL.create_policy(data)

    @staticmethod
    def get_policy(policy_number):
        return PolicyDAL.get_policy_by_number(policy_number)

    @staticmethod
    def update_policy(policy_number, data):
        return PolicyDAL.update_policy(policy_number, data)

    @staticmethod
    def delete_policy(policy_number):
        return PolicyDAL.delete_policy(policy_number)
