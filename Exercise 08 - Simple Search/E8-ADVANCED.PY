## Exercise 8: Simple Search - 30 Marks

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user for a name to search
search_name = input("Enter a name to search for: ")

found = False

# Search through the list
for name in names:
    if name.lower() == search_name.lower():
        found = True
        break

# Output result
if found:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")
