from models.status import Status
from app import db

class StatusDAL:

    @staticmethod
    def create_status(data):
        new_status = Status(
            status=data['status']
        )
        db.session.add(new_status)
        db.session.commit()
        return new_status

    @staticmethod
    def get_status_by_id(status_id):
        return Status.query.get(status_id)

    @staticmethod
    def update_status(status_id, data):
        status = Status.query.get(status_id)
        if status:
            status.status = data.get('status', status.status)
            db.session.commit()
        return status

    @staticmethod
    def delete_status(status_id):
        status = Status.query.get(status_id)
        if status:
            db.session.delete(status)
            db.session.commit()
        return status
