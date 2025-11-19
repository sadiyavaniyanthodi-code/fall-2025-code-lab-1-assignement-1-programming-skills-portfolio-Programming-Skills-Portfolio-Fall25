## Exercise 3: Biography - 25 Marks

#Making the user input the details
Name = str(input("Enter your name:"))
Hometown = str(input("Enter your hometown:"))
#Safely convert age to an integar
while True:
    age_input = (input("Enter your age:"))
    if age_input.isdigit():
        Age= int(age_input)
        break
    else:
        print("Please enter a valid age.")
#Storing the information in a dictionary        
your_info={
    "Name":Name,
    "Hometown":Hometown,
    "Age":Age,}
#Print the values
print(f"Name:{your_info['Name']}\nHometown:{your_info['Hometown']}\nAge:{your_info['Age']}")

