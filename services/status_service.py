from dal.status_dal import StatusDAL

class StatusService:

    @staticmethod
    def create_status(data):
        return StatusDAL.create_status(data)

    @staticmethod
    def get_status(status_id):
        return StatusDAL.get_status_by_id(status_id)

    @staticmethod
    def update_status(status_id, data):
        return StatusDAL.update_status(status_id, data)

    @staticmethod
    def delete_status(status_id):
        return StatusDAL.delete_status(status_id)
