"""
auth.py

Handles login and user authentication.
"""

class AuthManager:
    def __init__(self, database):
        self.database = database


    # =====================================
    # Login
    # =====================================

    def login(self, username, password):

        username = username.strip().lower()

        user = self.database.find_user(username)

        if user is None:
            return None

        db_username, db_password, role, roll = user

        if password != db_password:
            return None

        return {
            "username": db_username,
            "role": role,
            "roll": roll
        }
    
if __name__ == "__main__":

    from sqlite_database import SQLiteDatabase

    database = SQLiteDatabase()

    auth = AuthManager(database)

    username = input("Username : ")
    password = input("Password : ")

    user = auth.login(username, password)

    if user:

        print("\nLogin Successful!")
        print("Username :", user["username"])
        print("Role     :", user["role"])

    else:

        print("\nInvalid Username Or Password")