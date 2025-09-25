import random
import string

def generate_password(length=12):
    """Create a random password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 Your mystery password is:")
    print(generate_password())