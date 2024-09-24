from dal.user_dal import UserDAL

class UserService:
    @staticmethod
    def register_user(email, password):
        # Add any validation or business logic here
        return UserDAL.create_user(email, password)

    @staticmethod
    def authenticate_user(email, password):
        user = UserDAL.get_user_by_email(email)
        if user and user.password == password:
            return user
        return None
