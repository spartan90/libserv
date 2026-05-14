"""Login Service is responsible to validate the user based on its userid and password for libserv application"""

class AuthenticationService:
    def __init__(self):
        # Mock Data # In actual system read it from db
        self._libserv_users = {
            "rohit": "rohit123",
            "asha": "asha123",
            "indrajit": "indrajit123",
            "test": "test"
        }

    ##check if user is a valid user
    def is_valid_user(self, user_id, password):
        if user_id in self._libserv_users:
            return self._libserv_users[user_id] == password
        return False
