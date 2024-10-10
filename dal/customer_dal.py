from models.customer import Customer
from app import db

class CustomerDAL:

    @staticmethod
    def create_customer(data):
        new_customer = Customer(
            customer_number=data['customer_number'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            zipcode=data['zipcode']
        )
        db.session.add(new_customer)
        db.session.commit()
        return new_customer

    @staticmethod
    def get_customer_by_number(customer_number):
        return Customer.query.get(customer_number)

    @staticmethod
    def update_customer(customer_number, data):
        customer = Customer.query.get(customer_number)
        if customer:
            customer.first_name = data.get('first_name', customer.first_name)
            customer.last_name = data.get('last_name', customer.last_name)
            customer.zipcode = data.get('zipcode', customer.zipcode)
            db.session.commit()
        return customer

    @staticmethod
    def delete_customer(customer_number):
        customer = Customer.query.get(customer_number)
        if customer:
            db.session.delete(customer)
            db.session.commit()
        return customer
