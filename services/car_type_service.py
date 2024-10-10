from dal.car_type_dal import CarTypeDAL

class CarTypeService:

    @staticmethod
    def create_car_type(data):
        return CarTypeDAL.create_car_type(data)

    @staticmethod
    def get_car_type(car_type_id):
        return CarTypeDAL.get_car_type_by_id(car_type_id)

    @staticmethod
    def update_car_type(car_type_id, data):
        return CarTypeDAL.update_car_type(car_type_id, data)

    @staticmethod
    def delete_car_type(car_type_id):
        return CarTypeDAL.delete_car_type(car_type_id)
