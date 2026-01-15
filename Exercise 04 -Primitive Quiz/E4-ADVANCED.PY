## Exercise 4: Primitive Quiz - 30 Marks

# Dictionary of European countries and their capitals
countries = {
    "Georgia": "tbilisi",
    "Latvia": "riga",
    "Greece": "athens",
    "Germany": "berlin",
    "Serbia": "belgrade",
    "Netherlands": "amsterdam",
    "Switzerland": "bern",
    "Belgium": "brussels",
    "Vatican City": "vatican city",
    "Ireland": "dublin"
}

score = 0

print("=== European Capitals Quiz ===\n")

# Loop through the quiz
for country, capital in countries.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()

    if answer == capital:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. The correct answer is {capital.title()}.\n")

# Display final score
print(f"Final Score: {score} / {len(countries)}")