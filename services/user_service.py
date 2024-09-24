from dal.user_dal import UserDAL
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def register_user(email, password):
        # Check if the email already exists
        if UserDAL.get_user_by_email(email):  # Assuming this method checks for existing users
            return {"success": False, "message": "Email already registered."}

        # If email is not registered, create the user
        hashed_password = generate_password_hash(password)
        user = UserDAL.create_user(email, hashed_password)
        return {"success": True, "user": user}

    @staticmethod
    def authenticate_user(email, password):
        user = UserDAL.get_user_by_email(email)
        if user and user.password == password:
            return user
        return None
