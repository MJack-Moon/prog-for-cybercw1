
"""
Banner: B01886621
Name: Matthew Newnham

"""


def ip_address_validator(): ## main function to validate the password

    while True:

        ip_address = input("Enter an IP address: ")
        if validate_ip(ip_address): ##sends the input to the validate_ip function and checks if it returns True or False
            print("Valid IP address")
            break
        else:
            print("Invalid IP address, try again.")

def validate_ip(ip): ## seperated for True/False validation, hardcoding givin name/pw

    ip = ip.strip() ##removes leading and trailing whitespace

    if "." not in ip: ## checks if the IP address contains dots
        return False

    if ip.count(".") != 3: ## checks if there are exactly three dots
        return False

    parts = ip.split(".") ## splits the IP address into four parts

    if len(parts) != 4: ## checks that there are four parts
        return False

    for part in parts: ## checks that the part contains only digits using for loop to iterate through each part of the IP address

        if not part.isdigit(): ## checks if the part is a digit
            return False
        
        number = int(part) ## converts the part to an integer

        if number < 0 or number > 255: ## checks that the number is between 0 and 255
            return False

    return True

def replay():
    while True:
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == "y" or play_again == "yes":
            print("Starting a new password validation...\n")
            ip_address_validator()
        elif play_again == "n" or play_again == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
if __name__ == "__main__":
    ip_address_validator()
    replay()
