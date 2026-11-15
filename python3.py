
# PASSWORD GENERATOR

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# Main program
print("--- Random Password Generator ---")

try:
    length = int(input("Enter a password length: "))

    if length < 4:
        print("Length should be at least 4!")

    else:
        pwd = generate_password(length)
        print("Generated Password:", pwd)

except ValueError:
    print("Please enter a valid number!")
