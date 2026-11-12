"""
Banner: B01886621
Name: Matthew Newnham

"""

"""
for each pass or fail, create/update a security log csv file
"""

import csv  # importing the csv module to handle reading and writing CSV files
import os  # importing the os module to handle file and directory operations
import socket  # importing the socket module to retrieve the host name and IP address
from datetime import (
    datetime,
)  # import datetime #importing the datetime module to get the current date and time
import sys  # importing the sys module to handle system-specific parameters and functions

fname = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "security_log.csv"
)  ## seting the file path to be in the same location as the .py file

"""
This function has been changed to start at the end of the file and step back one, so it's not reading through the whole file! makes it quicker on large files
I'm quite happy with this change :D
"""


def get_next_id(filename=fname):

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        return 1  # If the file doesn't exist or is empty, start with ID 1

    with open(filename, "r") as file:
        lines = file.readlines()
        if len(lines) <= 1:  # if only the header exists
            return 1

        last_line = lines[-1]  # Get the last line of the file
        last_id = int(last_line.split(",")[0])  # Extract the ID from the last line
        return last_id + 1  # Increment the ID for the next entry


def Security_event_logger():
    username = "admin"
    pw = "Pa$$w0rd"

    # if file dose not exsist, then creates ti with the listed headers bellow
    if not os.path.exists(fname) or os.path.getsize(fname) == 0:
        with open(fname, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["event_id", "uname", "login", "status", "ip", "event_time"]
            )
    while True:

        host = socket.gethostname()  ## pulls host name
        ip = socket.gethostbyname(host)  ## pulls ip using host name
        event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  ## pulls date/time

        # Basic user input, no validation as it's for passoword
        uname = input("\nEnter your username: ")
        passd = input("Enter your password: ")

        if uname == username and passd == pw:
            status = "success"
            print("\nLogin approved\nWelcome Admin.")

        else:
            status = "failed"
            print("\nUsername or password invalid")

        # with the file open "a" appends the contents of the program to the file as listed. note, "login" is a header but not a value input only a string
        event_id = get_next_id(fname)
        with open(fname, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([event_id, uname, "login", status, ip, event_time])
            print("Log created")

        if status == "success":  # if successful moves to
            display_menu()
            break


def display_menu():  # small menu for login success with options for displaying already generated log or logout that leads to replay function"
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Display security log")
        print("2. Log out")

        choice = input("Select an option: ")

        if choice == "1":
            display_log()

        elif choice == "2":
            print("\nLogging out...")
            replay()
            break

        else:
            print("Invalid option. Please select 1 or 2.")


def replay():  #  #replay function to allow user to play again or exit the program
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again in ("y", "yes"):
        print("\nStarting a new password validation...\n")
        Security_event_logger()

    elif play_again in ("n", "no"):
        print("\nThanks for playing!")
        sys.exit()  ## forces exit from the program

    else:
        print("Invalid input. Please select an option")


def display_log():  # Displays the current security log saved to the system
    if not os.path.exists(fname) or os.path.getsize(fname) == 0:
        print("\nNo security log available.")
        return

    print("\n========== SECURITY LOG ==========")

    with open(fname, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

    print("==================================")


if __name__ == "__main__":
    Security_event_logger()
