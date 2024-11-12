# Password Generator:
# 1) Ask user what minimum length is.
# 2) Do they want numbers/special chars included.
    # If so password must contain one of each.
# 3) Generate the password.

import string
import random

# Generate Password | The choice to include numbers and special chars have a default value of true
def generate_password(min_length, numbers=True, special_characters=True):
    
    # Using String module grab all possible letters/digits/special_chars
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Combine all into a list to randomly choose from.
    # Created string should only contain what we have specified is allowed.
    # Password will always contain letters.
    
    # Characters initially contains letters and we can append the digits and special list if they are set to true.
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Password Var | Set to true when specified criteria is met | Set to true if contains number/special
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    # Loop to generate and add a random character from "characters" to our password.
    while not meets_criteria or len(password) < min_length:

        new_char = random.choice(characters)
        password += new_char

        # If password now contains a digit/special set has_number/has_special to true.
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Update when criteria is met:
        meets_criteria = True
        
        # If we should have a number...
        if numbers:
            # Set to True if we have a number
            meets_criteria = has_number
        
        # If we should have a special char 
        if special_characters:
            # Set to true if we are currently meeting the criteria AND we have a special char
            meets_criteria = meets_criteria and has_special

    return password

# Get user criteria
def user_criteria():
    
    min_length = int(input("Enter password length: \n"))

    # User enters anything other than y/Y we will not include numbers/special chars
    numbers = input("Include Numbers (Y/N): \n").lower() == "y"
    special_characters = input("Include Specials (Y/N): \n").lower() == "y"

    return min_length, numbers, special_characters

# Prompt user for criteria:
min_length, numbers, special_characters = user_criteria()

# Generate & print password
password = generate_password(min_length, numbers, special_characters)
print("GENERATED PASSWORD: \n", password)