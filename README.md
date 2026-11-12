# Student information
### Banner:  B01886621
### Name:    Matthew Newnham
### Campus:  NCL Motherwell
### module:  COMP08101

# Program description 

This program requires both files within the repo.
"main.py" contains the main running program that will be ran.
"security_tools.py" contains all the module functions that will be called by "main.py" ensure both are within the same location.

The main program handles user interaction, while the imported module contains the functions responsible for IP address validation, password validation and secure random password generation.

# Design of the program

## security_tools.py

1. ### IP address validator

   - Takes a provided IPv4 address
   - Checks the provided IPv4 address that it meets all requirements of an ipv4 address
   - Returns True or False
   - Tells user if it's valid

2. ### Password validator
   - Takes a provided password
   - Runs the password against standard password requirements
   - Returns True or False
   - Tells user if it's valid
  
3. ### Random password generater
   - If ip address validator returns False this function runs
   - Asks the user if they want a passowrd generated
   - If user answers yes the program will provide the user with a generated password within standard password requirements

## main.py

- gets IP address and password from user
- Calls and passes user input into both functions
- Takes the output from the functions and displays if inputs were valid
- If password was not valid, asks the user if they want a generated password
- If yes, calls the password generation function

## How to run programs 

1. Open a terminal in the repository.

2. Switch to the correct branch:
```bash
git switch cyber-security-utilities
```
3. Make sure main.py and security_tools.py are in the same directory.

4. Run the main program:
```bash
python main.py
```
5. Enter an IP address and password.

6. Review the validation results.

7. If the password is invalid, choose whether to generate a random password.

8. Follow the replay prompt to restart or exit.
  
     
