# prog-for-cybercw1

## Student Information

# Name: Matthew Newnham


# Security tool


## Program Description

This Python program provides a menu-driven security tool containing three different cybersecurity functions.

The program demonstrates password checking, authentication, loops, conditional statements, functions and basic security event analysis.

## Features

### 1. Security Event Counter
- Requests ten password entries from the user.
- Compares each entry against a predefined password.
- Counts successful and unsuccessful entries.
- Calculates the percentage of incorrect password attempts.
- Displays a security alert when more than 50% of attempts are incorrect.

### 2. Brute-Force Simulation
- Simulates a password guessing scenario.
- Allows a maximum of three attempts.
- Displays the number of remaining attempts.
- Displays a simulated account-lockout message if all attempts fail.

### 3. Login Authentication
- Requests a username and password.
- Compares the credentials against predefined values.
- Allows a maximum of three unsuccessful attempts.
- Displays whether authentication succeeds or fails.
- Simulates an account freeze after three failed attempts.

## How to Run

1. Open a terminal in the repository.
2. Switch to the correct branch:

   ```bash
   git switch security-tool
   ```

3. Run the Python program:

   ```bash
   python security_tool.py
   ```

4. Select an option from the menu and follow the instructions.

## Python Concepts Demonstrated

- Functions
- Conditional statements (`if`, `elif`, `else`)
- `for` loops and `while` loops
- User input and output
- Variables and counters
- Percentage calculations
- String comparisons
