from dal.customer_dal import CustomerDAL

class CustomerService:

    @staticmethod
    def create_customer(data):
        return CustomerDAL.create_customer(data)

    @staticmethod
    def get_customer(customer_number):
        return CustomerDAL.get_customer_by_number(customer_number)

    @staticmethod
    def update_customer(customer_number, data):
        return CustomerDAL.update_customer(customer_number, data)

    @staticmethod
    def delete_customer(customer_number):
        return CustomerDAL.delete_customer(customer_number)
