## Exercise 6: Brute Force Attack - 30 Marks

# Define the correct password
correct_password = "12345"

# Ask for the password until it is correct
while True:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted. Correct password entered.")
        break
    else:
        print("Incorrect password. Try again.")