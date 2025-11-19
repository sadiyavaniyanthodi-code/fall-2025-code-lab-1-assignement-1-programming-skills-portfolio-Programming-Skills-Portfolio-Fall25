## Exercise 8: Simple Search - 30 Marks

#Creating a list of names
names = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]
#Asking the user to search for a name
search_names = input("Enter your name:")
#checking the name that user entered
if search_names in names:
    print(f"{search_names} is there on the list")
else:
    print(f"{search_names} is not there in the world")
