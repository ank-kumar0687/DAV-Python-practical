# Write a program to create a list of names; then define a function 
# to display all the elements in the received list. Call the function to 
# execute its statements and display all names in the list.



names_list = ["Ankit", "Ankush", "Aftab", "Ravi"]


def display_names(list_of_names):
    print("Printing names from the list:")
    for name in list_of_names:
        print(name)


display_names(names_list)