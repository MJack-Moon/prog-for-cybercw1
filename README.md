# Student information
### Banner:  B01886621
### Name:    Matthew Newnham
### Campus:  NCL Motherwell
### module:  COMP08101

# Ip address validator

This program is designed to take an ipv4 address provided by the users.
The program checks if the ipv4 address meets all the requirements to be a valid ipv4 address,
It will continue to run till a valid ipv4 address is provided, such as:

```bash
192.168.50.50
```
## Design of the program

- Asks for an IPv4 address from the user.

- Removes leading and trailing whitespace.

- Checks that the address contains exactly three dots.

- Splits the address into four sections.

- Checks that each section contains numerical digits.

- Ensures each section has a value between 0 and 255.

- Rejects leading zeros in multi-digit sections.

- Displays whether the address is valid.

- Allows the user to repeat the validation process.

## Running the program 

1. Open a terminal in the repository.

2. Switch to the correct branch:
```bash
git switch ip-address-validator
```
3. Run the program:

```bash
python ip_address_validator.py
```
4. Enter an IPv4 address when prompted.

5. If the address is invalid, enter another.

