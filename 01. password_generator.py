import string
import random

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

y = generate_password()
print(y)