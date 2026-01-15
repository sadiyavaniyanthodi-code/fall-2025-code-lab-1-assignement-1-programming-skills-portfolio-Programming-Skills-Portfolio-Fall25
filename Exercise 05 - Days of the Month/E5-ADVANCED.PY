## Exercise 5: Days of the Month - 30 Marks

# Dictionary mapping month numbers to days
days_in_month = {
    1: 31,
    2: 28,  
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for a month number
month = int(input("Enter a month number (1-12): "))

# Check if the month is valid
if month in days_in_month:
    # Special case for February
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        print(f"This month has {days_in_month[month]} days.")
else:
    print("Invalid month number.")