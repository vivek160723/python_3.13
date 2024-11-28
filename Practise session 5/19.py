# Create a function to generate a random password with a given length,
# ensuring a mix of uppercase, lowercase, digits, and special characters.


import random
import string


def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)


# Example usage
password = generate_password(12)
print(password)