from extensions import db
from models.user import User

class UserDAL:
    @staticmethod
    def create_user(email, password):
        new_user = User(email=email, password=password)  # Store plain password
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
