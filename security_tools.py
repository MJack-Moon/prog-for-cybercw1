"""
Banner: B01886621
Name: Matthew Newnham

"""



#Reusable cyber security utilities

import secrets # used for generating secure random numbers
import string # used for string manipulation and character sets



    



def ip_address_validator(ask_ip): ## IP address validation function

    ip = ask_ip.strip() ## removes leading and trailing whitespace

    if "." not in ip: ## checks if the IP address contains dots
        return False

    if ip.count(".") != 3: ## checks if there are exactly three dots
        return False

    parts = ip.split(".") ## splits the IP address into four parts

    if len(parts) != 4: ## checks that there are four parts
        return False

    for part in parts: ## checks each part of the IP address

        if not part.isdigit(): ## checks if the part contains only digits
            return False

        if len(part) > 1 and part.startswith("0"): ## checks for leading zeros
            return False

        number = int(part) ## converts the part to an integer

        if number < 0 or number > 255: ## checks that the number is between 0 and 255
            return False

    return True


def gen_password(): # generating the password

    #allowed symbles and characters for password generation
    allowed_s = "!@#$%"  ## setting the allowed symbols for password validation
    upper = string.ascii_uppercase  ## uppercase letters
    lower = string.ascii_lowercase  ## lowercase letters
    digits = string.digits  ## digits 0-9

    pass_length = secrets.randbelow(7) + 10  ## random length between 10 and 16

    #making list for the password to ensure at least one of each required character type is included
    password = []

    # ensuring at least one of each required character type is included
    password.append(secrets.choice(upper))  ## ensuring at least one uppercase letter
    password.append(secrets.choice(lower))  ## ensuring at least one lowercase letter
    password.append(secrets.choice(digits))  ## ensuring at least one digit
    password.append(secrets.choice(digits))
    password.append(secrets.choice(allowed_s))  ## ensuring at least one symbol

    allowed_chars = upper + lower + digits + allowed_s  ## all allowed characters for password generation

    while len(password) < pass_length:  ## filling the rest of the password with random allowed characters
        password.append(secrets.choice(allowed_chars))

    secrets.SystemRandom().shuffle(password)  ## shuffling the password so it's random

    return ''.join(password)

    
def Password_valid(ask_password):

    password = ask_password  ## calling the password generation function

    allowed_symbols = "!@#$%"  ## setting the allowed symbols for password validation




    length = len(password)  ## calculating the length of the password

    uppercase_count = sum(
        1 for char in password if char.isupper()
    )  ## counting the number of uppercase letters in the password

    lowercase_count = sum(
        1 for char in password if char.islower()
    )  ## counting the number of lowercase letters in the password

    number_count = sum(
        1 for char in password if char.isdigit()
    )  ## counting the number of digits in the password

    symbol_count = sum(
        1 for char in password if char in allowed_symbols
    )  ## counting the number of symbols in the password

    space_count = sum(
        1 for char in password if char.isspace()
    )  ## counting the number of spaces in the password

    if length < 10:
        print("Password must be at least 10 characters long.")
        return False

    if uppercase_count < 1:
        print("Password must contain at least 1 uppercase letter.")
        return False

    if lowercase_count < 1:
        print("Password must contain at least 1 lowercase letter.")
        return False

    if number_count < 2:
        print("Password must contain at least 2 digits.")
        return False

    if symbol_count < 1:
        print("Password must contain at least 1 symbol from the list: !, @, #, $, %.")

        return False

    if any(char not in allowed_symbols and not char.isalnum() for char in password):  ## valadation for the allowed symbles provided
        print("Password must contain the following symbols: !, @, #, $, %.")
        return False

    if space_count > 0:
        print("Password must not contain any spaces.")
        return False



    
    return True
