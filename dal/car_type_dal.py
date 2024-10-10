from models.car_type import CarType
from app import db

class CarTypeDAL:

    @staticmethod
    def create_car_type(data):
        new_car_type = CarType(
            car_make=data['car_make'],
            car_model=data['car_model']
        )
        db.session.add(new_car_type)
        db.session.commit()
        return new_car_type

    @staticmethod
    def get_car_type_by_id(car_type_id):
        return CarType.query.get(car_type_id)

    @staticmethod
    def update_car_type(car_type_id, data):
        car_type = CarType.query.get(car_type_id)
        if car_type:
            car_type.car_make = data.get('car_make', car_type.car_make)
            car_type.car_model = data.get('car_model', car_type.car_model)
            db.session.commit()
        return car_type

    @staticmethod
    def delete_car_type(car_type_id):
        car_type = CarType.query.get(car_type_id)
        if car_type:
            db.session.delete(car_type)
            db.session.commit()
        return car_type
