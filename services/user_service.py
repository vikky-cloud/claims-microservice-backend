from werkzeug.security import generate_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from dal.user_dal import UserDAL

class UserService:
    @staticmethod
    def register_user(email, password):
        # Check if the email already exists
        if UserDAL.get_user_by_email(email):  # Assuming this method checks for existing users
            return {"success": False, "message": "Email already registered."}

        # If email is not registered, create the user
        user = UserDAL.create_user(email, password)
        return {"success": True, "user": user}

    @staticmethod
    def login_user(email, password):
        user = UserDAL.get_user_by_email(email)  # Retrieve user from the database
        if user and check_password_hash(user.password, password):  # Check password
            return {"success": True, "user": user}
        return {"success": False, "message": "Invalid credentials"}
