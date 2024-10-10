from dal.claim_dal import ClaimDAL

class ClaimService:

    @staticmethod
    def create_claim(data):
        return ClaimDAL.create_claim(data)

    @staticmethod
    def get_claim(claim_number):
        return ClaimDAL.get_claim_by_id(claim_number)

    @staticmethod
    def update_claim(claim_number, data):
        return ClaimDAL.update_claim(claim_number, data)

    @staticmethod
    def delete_claim(claim_number):
        return ClaimDAL.delete_claim(claim_number)
