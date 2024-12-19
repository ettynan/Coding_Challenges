'''Create a program that checks if a given string is a valid email address'''

import re

def is_valid_email(email):
    # Regular expression pattern for validating email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

# Example usage
email = "test@example.com"
print(f"Is '{email}' a valid email? {is_valid_email(email)}")

email = "invalid-email"
print(f"Is '{email}' a valid email? {is_valid_email(email)}")
