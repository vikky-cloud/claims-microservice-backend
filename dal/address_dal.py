from models.address import Address
from app import db

class AddressDAL:

    @staticmethod
    def create_address(data):
        new_address = Address(
            zipcode=data['zipcode'],
            street_address=data['street_address'],
            city=data['city'],
            state=data['state']
        )
        db.session.add(new_address)
        db.session.commit()
        return new_address

    @staticmethod
    def get_address_by_zipcode(zipcode):
        return Address.query.get(zipcode)

    @staticmethod
    def update_address(zipcode, data):
        address = Address.query.get(zipcode)
        if address:
            address.street_address = data.get('street_address', address.street_address)
            address.city = data.get('city', address.city)
            address.state = data.get('state', address.state)
            db.session.commit()
        return address

    @staticmethod
    def delete_address(zipcode):
        address = Address.query.get(zipcode)
        if address:
            db.session.delete(address)
            db.session.commit()
        return address
