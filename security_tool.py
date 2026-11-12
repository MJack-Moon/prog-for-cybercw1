"""
Banner: B01886621
Name: Matthew Newnham

"""


def display_menu():  ## Display the security tool menu and handle user selection

    print("\nSecurity Tool Menu:")

    print("1. Security Event Counter")

    print("2. Brute-Force Simulation")

    print("3. Login Authentication")

    print("4. Exit")

    input_user = input(
        "Please select an option (1-4): "
    )  ## Get user input for menu selection from the user with 1-4 sellecting the tool function to run

    if input_user == "1":
        security_event_counter()  ## Call the function to execute the security event counter

    elif input_user == "2":
        brute_force_simulation()  ## Call the function to execute the brute force simulation

    elif input_user == "3":
        login_authentication()  ## Call the function to execute the login authentication

    elif input_user == "4":  ### Call the function to exit the program
        exit_program()

    else:
        print("Invalid selection. Please choose a valid option.")


def security_event_counter():  ## Count correct and incorrect password entries and display statistics

    correct_password = "Pa$$w0rd"  # Predefined correct password
    correct_count = 0
    incorrect_count = 0
    for _ in range(10):
        password = input("Enter password: ")
        if password == correct_password:
            correct_count += 1
        else:
            incorrect_count += 1

    print(f"\nCorrect passwords entered: {correct_count}")
    print(f"Incorrect passwords entered: {incorrect_count}")

    if incorrect_count > 0:
        incorrect_percentage = (incorrect_count / 10) * 100
        print(f"Percentage of incorrect passwords: {incorrect_percentage:.2f}%")
        if incorrect_percentage > 50:
            print("Alert: More than 50% of passwords entered were incorrect.")


def brute_force_simulation():  ## Simulate a brute-force password guessing scenario with limited attempts

    correct_password = "Pa$$w0rd"  # Predefined correct password
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        password = input("Enter password guess: ")
        attempts += 1
        if password == correct_password:
            print("\nCorrect password entered!")
            break
        else:
            print(f"Incorrect password.\n Attempts left: {max_attempts - attempts}")

    if attempts == max_attempts:
        print(
            "\nMaximum attempts reached.\nAccount has been locked.\nContact your system administrator for assistance."
        )


def login_authentication():  ## Authenticate user login credentials
    correct_username = "admin"
    correct_password = "Pa$$w0rd"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == correct_username and password == correct_password:
            print("Authentication succeeded!")
            break
        else:
            attempts += 1
            print(
                f"Authentication failed\nUsername or password is incorrect.\nAttempts left: {max_attempts - attempts}"
            )

    if attempts == max_attempts:
        print("Account frozen for 24 hours due to too many failed login attempts.")


def exit_program():  ### Exit the program with a thank you message
    print("Thank you for using the security tool.")
    quit()


if __name__ == "__main__":
    display_menu()  # Call the function to execute the program
