import string
import random

def generate_password(length):
    # Define the character sets to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user to enter the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if _name_ == "_main_":
    main()