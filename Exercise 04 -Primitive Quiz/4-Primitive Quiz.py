## Exercise 4: Primitive Quiz - 30 Marks

#Storing countries and their capitals in a dictionary
countries = {
    "Georgia": "Tbilisi",
    "Latvia": "Riga",
    "Greece": "Athens",
    "Germany": "Berlin",
    "Serbia": "Belgrade",
    "Netherlands": "Amsterdam",
    "Switzerland": "Bern",
    "Belgium": "Brussels",
    "Vatican City": "Vatican City",
    "Ireland": "Dublin"
}
#Initializing score counter
marks = 0
#Asking the questions
for country, capital in countries.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.strip().lower() == capital.lower():
        print("The answer you entered is correct!")
        marks += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")
#Printing the total score        
print(f"\nYou got {marks} out of {len(countries)} correct!")

