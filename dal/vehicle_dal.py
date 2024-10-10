from models.vehicle import Vehicle
from app import db

class VehicleDAL:

    @staticmethod
    def create_vehicle(data):
        new_vehicle = Vehicle(
            VIN=data['VIN'],
            model_year=data['model_year'],
            car_type_id=data['car_type_id']
        )
        db.session.add(new_vehicle)
        db.session.commit()
        return new_vehicle

    @staticmethod
    def get_vehicle_by_vin(VIN):
        return Vehicle.query.get(VIN)

    @staticmethod
    def update_vehicle(VIN, data):
        vehicle = Vehicle.query.get(VIN)
        if vehicle:
            vehicle.model_year = data.get('model_year', vehicle.model_year)
            vehicle.car_type_id = data.get('car_type_id', vehicle.car_type_id)
            db.session.commit()
        return vehicle

    @staticmethod
    def delete_vehicle(VIN):
        vehicle = Vehicle.query.get(VIN)
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
        return vehicle
