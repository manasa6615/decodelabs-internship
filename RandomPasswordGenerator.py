import string
import secrets

try:
    length = int(input("Enter the desired password length (e.g., 16): "))
    
    if length < 6:
        print("Error: Password is too short for basic security.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        
        password = ''.join(secrets.choice(characters) for i in range(length))
        
        print(f"Your secure password is: {password}")

except ValueError:
    print("Invalid input! Please enter a numerical value for the length.")
    