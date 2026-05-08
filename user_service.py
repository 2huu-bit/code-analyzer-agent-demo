from utils import validate_email, format_name

class UserService:
    def __init__(self):
        self.users = []
    
    def add_user(self, first, last, email):
        if not validate_email(email):
            raise ValueError("Invalid email")
        name = format_name(first, last)
        self.users.append({"name": name, "email": email})
        return len(self.users) - 1
    
    def get_user(self, index):
        return self.users[index] if index < len(self.users) else None