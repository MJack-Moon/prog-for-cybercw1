"""
Banner: B01886621
Name: Matthew Newnham

"""

import security_tools  ## Import the security_tools module to access its functions


def display_menu():

    while True:

        ask_ip = input(
            "Enter an IP address: "
        )  ## Prompt the user to enter an IP address
        ask_password = input(
            "Enter a password: "
        )  ## Prompt the user to enter a password

        if security_tools.ip_address_validator(
            ask_ip
        ):  ## Validate the IP address using the ip_address_validator function from security_tools
            print("IP input is valid.")
        else:
            print("IP input is invalid.")

        if (
            security_tools.Password_valid(ask_password) == True
        ):  ## Validate the password using the Password_valid function from security_tools
            print("Password is valid.")
        else:
            print("Password is invalid.")

            ask = input(
                "Would you like a random passowrd? yes or no: "
            )  ## Prompt the user to ask if they want a random password
            if ask.lower().strip() in [
                "yes",
                "y",
            ]:  ## Check if the user input is "yes" or "y"
                random_password = (
                    security_tools.gen_password()
                )  ## Generate a random password using the gen_password function from security_tools
                print(
                    "Randomly generated password:", random_password
                )  ## Display the randomly generated password

            else:
                break  ## Exit the loop if the user does not want a random password
        break  ## Exit the loop after one iteration of IP and password validation


def replay():
    while True:
        play_again = input("Would you like to play again? (y/n): ").lower().strip()

        if play_again == "y" or play_again == "yes":
            print("Restarting...\n")
            display_menu()

        elif play_again == "n" or play_again == "no":
            print("Thanks for playing!")
            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    display_menu()
    replay()
