## Exercise 6: Brute Force Attack - 30 Marks

# Define the correct password
correct_password = "12345"

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted. Correct password entered.")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts

        if remaining > 0:
            print(f"Incorrect password. {remaining} attempts remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")