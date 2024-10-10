from dal.address_dal import AddressDAL

class AddressService:

    @staticmethod
    def create_address(data):
        return AddressDAL.create_address(data)

    @staticmethod
    def get_address(zipcode):
        return AddressDAL.get_address_by_zipcode(zipcode)

    @staticmethod
    def update_address(zipcode, data):
        return AddressDAL.update_address(zipcode, data)

    @staticmethod
    def delete_address(zipcode):
        return AddressDAL.delete_address(zipcode)
