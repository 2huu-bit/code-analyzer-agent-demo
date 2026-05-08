def validate_email(email):
    return "@" in email and "." in email.split("@")[-1]

def format_name(first, last):
    return f"{first.capitalize()} {last.capitalize()}"