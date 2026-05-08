from user_service import UserService

def main():
    service = UserService()
    user_id = service.add_user("john", "doe", "john@example.com")
    print(f"Created user: {service.get_user(user_id)}")

if __name__ == "__main__":
    main()