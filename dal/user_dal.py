from models.user import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class UserDAL:
    @staticmethod
    def create_user(email, password):
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
