"""
Banner: B01886621
Name: Matthew Newnham

"""


import sys


def interface():

    while True:  # Loop to prompt the user to select an option until a valid option is selected

            security_incident = {  # Creating dictionary with key-value pairs for username, IP address, event type and risk level
                "username": "user123",
                "ip_address": "192.168.1.1",
                "event_type": "unauthorized access",
                "risk_level": "high",
            }
            print("==== Security Incident Manager ====\n")
            print(
                "IP Address:", security_incident["ip_address"]
            )  # printing the IP address from the dictionary using the key "ip_address"
            print(
                "username:", security_incident["username"]
            )  # printing the username from the dictionary using the key "username"
            # Call other functions with the dictionary as an argument to update and display the security incident information
            status(security_incident)
            risk_level(security_incident)
            remove_field(security_incident)
            display_remaining(security_incident)
            break  # Exit the loop after one iteration to prevent infinite loop
    replay()  # Call the replay function to ask the user if they want to play again
def status(
    security_incident,
):  # Function to add a new field called status to the security incident dictionary
    print("==== Security Incident Status Update ====\n")
    print("Select a status for the security incident:\n")
    print("1. Open")
    print("2. Under Investigation")
    print("3. Resolved")
    print("4. Closed\n")

    while (
        True
    ):  ## Loop to prompt the user to select a status for the security incident until a valid option is selected
        try:
            status_optipn = int(input("Select an option for the status, 1 - 4 "))

            if (
                status_optipn < 1 or status_optipn > 4
            ):  # Checking if the user input is valid (between 1 and 4)
                print(
                    "Invalid option selected. Please select a valid option between 1 and 4."
                )
                continue

            if status_optipn == 1:
                state = "Open"
            elif status_optipn == 2:
                state = "Under Investigation"
            elif status_optipn == 3:
                state = "Resolved"
            elif status_optipn == 4:
                state = "Closed"

            security_incident["status"] = (
                state  ## Adding the new field "status" to the security incident dictionary with the selected value
            )
            return security_incident  ### Returning the updated security incident dictionary to the calling function

        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 4.")


# update the risk level of the security incident dictionary


def risk_level(
    security_incident,
):  # Function to update the risk level of the security incident dictionary
    print("==== Security Incident Risk Level Update ====\n")
    print("Select a status for the risk level:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("4. Critical\n")

    while True:
        try:
            risk_optipn = int(input("Select a risk assesment level, 1 - 4 "))

            if (
                risk_optipn < 1 or risk_optipn > 4
            ):  ## Checking if the user input is valid (between 1 and 4)
                print(
                    "Invalid option selected. Please select a valid option between 1 and 4."
                )
                continue

            if risk_optipn == 1:
                risk = "low"
            elif risk_optipn == 2:
                risk = "medium"
            elif risk_optipn == 3:
                risk = "high"
            elif risk_optipn == 4:
                risk = "critical"

            security_incident["risk_level"] = (
                risk  ## Updating the "risk_level" field in the security incident dictionary with the selected value
            )
            return security_incident  ### Returning the updated security incident dictionary to the calling function
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    # Remove one field from the dictionary


def remove_field(
    security_incident,
):  # Function to remove a field from the security incident dictionary
    print("==== Security Incident Field Removal ====\n")
    print("Select a field to remove from the security incident:")
    print("1. Username")
    print("2. IP Address")
    print("3. Event Type")
    print("4. Risk Level")
    print("5. Status")
    print("6. Remove none\n")

    while True:
        try:
            field_option = int(
                input("Select an option for the field to remove, 1 - 6 ")
            )

            if (
                field_option < 1 or field_option > 6
            ):  ## Checking if the user input is valid (between 1 and 6)
                print(
                    "Invalid option selected. Please select a valid option between 1 and 6."
                )
                continue

                """
                Each option corresponds to a field in the security incident dictionary. 
                If the user selects an option, the corresponding field will be removed from the dictionary using the del statement.
                If the user selects option 6, no fields will be removed and the function will exit.
                """
            if field_option == 1:
                if "username" in security_incident:
                    del security_incident["username"]
                else:
                    print("Username has already been removed.")

            elif field_option == 2:
                if "ip_address" in security_incident:
                    del security_incident["ip_address"]
                else:
                    print("IP Address has already been removed.")

            elif field_option == 3:
                if "event_type" in security_incident:
                    del security_incident["event_type"]
                else:
                    print("Event Type has already been removed.")

            elif field_option == 4:
                if "risk_level" in security_incident:
                    del security_incident["risk_level"]
                else:
                    print("Risk Level has already been removed.")

            elif field_option == 5:
                if "status" in security_incident:
                    del security_incident["status"]
                else:
                    print("Status has already been removed.")

            elif (
                field_option == 6
            ):  ## If the user selects option 6, no fields will be removed and the function will exit.
                print("Exiting field removal process.")

            return security_incident  #### Returning the updated security incident dictionary to the calling function
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


# display all
def display_remaining(
    security_incident,
):  # Function to display all remaining keys and values in the security incident dictionary
    print("\n==== Remaining Security Incident Details ====\n")
    for (
        key,
        value,
    ) in (
        security_incident.items()
    ):  ## Looping through the security incident dictionary and printing each key-value pair
        print(
            key, ":", value
        )  ### Printing the key and value of each key-value pair in the security incident dictionary

    ###printing the total number of key-value pairs in the security incident dictionary using the len() function
    print("Total number of key-value pairs:", len(security_incident))

def replay():  ## Replay function import file pending
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again in ("y", "yes"):
        print("\nStarting a new password validation.\n")
        interface()

    elif play_again in ("n", "no"):
        print("\nThanks for playing!")
        sys.exit()  ## forces exit from the program

    else:
        print("Invalid input. Please select an option")
        replay()  # Continue the loop to prompt the user again for a valid input

if __name__ == "__main__":
    interface()  