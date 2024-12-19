import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    # Create the pool of characters to choose from
    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# User input
def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter password length (e.g., 12): "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print("\nYour generated password is:")
        print(password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
