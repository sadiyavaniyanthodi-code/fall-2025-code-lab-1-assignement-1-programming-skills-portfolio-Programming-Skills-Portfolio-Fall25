## Exercise 3: Biography - 25 Marks

# Ask the user for their information
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

# Validate age input
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number for age.")

# Store the information in a dictionary
biography = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}

# Print all information using ONE print statement
print(
    "\n=== Biography Summary ===\n"
    f"Name: {biography['Name']}\n"
    f"Hometown: {biography['Hometown']}\n"
    f"Age: {biography['Age']}"
)
