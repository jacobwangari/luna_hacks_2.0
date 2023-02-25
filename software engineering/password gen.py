import random
import string

def generate_password():
    """
    Generate a strong password of the given length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate 16 characters password 
    password = ''.join(random.choices(characters,k=16))
    return password

# Example usage:
password = generate_password()
print(password)
