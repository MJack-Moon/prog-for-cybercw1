# Student information
### Banner:  B01886621
### Name:    Matthew Newnham
### Campus:  NCL Motherwell
### module:  COMP08101


# *Security event logger*



# Program Description

This program is designed to detect the login ip address and username entered into the program, details are then stored in a csv file.
The csv file if not already existing is created on first use. This file is is generated on your local machine and no information leaves the local machine.

# Program breakdown

## Login Authentication

- Requests a username and password.

- Compares the entered credentials against predefined values.

- Identifies successful and failed login attempts.

- Allows access to an administrative menu following successful authentication.

## Security Event Logging

- Automatically creates security_log.csv if it does not exist.

- Generates a sequential event ID for each new login attempt.

- Records the username and login result.

- Records an IP address resolved from the computer's hostname.

- Records the date and time of each attempt.

- Appends new events without deleting previous records.

## Security Log Viewer

- Gives an option to display recorded security events.

- Reads the existing CSV file.

- Displays the recorded fields in the terminal.

- CSV File Structure

### The program records the following fields:

- event id
- 
- username
- 
- event type
- 
- event status
- 
- ip address
- 
- time and date of event
  

