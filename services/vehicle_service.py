from dal.vehicle_dal import VehicleDAL

class VehicleService:

    @staticmethod
    def create_vehicle(data):
        return VehicleDAL.create_vehicle(data)

    @staticmethod
    def get_vehicle(VIN):
        return VehicleDAL.get_vehicle_by_vin(VIN)

    @staticmethod
    def update_vehicle(VIN, data):
        return VehicleDAL.update_vehicle(VIN, data)

    @staticmethod
    def delete_vehicle(VIN):
        return VehicleDAL.delete_vehicle(VIN)
