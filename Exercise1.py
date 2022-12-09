# Exercises
# 1) Create a program that allows a user to continue to add people to an address book until the user quits. Once the user quits, break out of the loop and print out the name and address of everyone in the address book
# Steps
# Create a function that will ask user for name and addresses and stores them in a dictionary
# Define an empty dictionary with which to work (global or local variable?)
# Begin a loop that will continue to ask a user for information until the user "quits"
# If the user does not quit, ask for a name and address and store the values into variables
# Add information to the dictionary with name as the key and address as the value
# If the user does quit, end the loop
# Print out the information from the dictionary in a formatted way
# Execute/Call the function



address_book = {}
def gather_info(x):
    while x != "n":
        full_name = input('what is full name?')
        address = input('what is the address?')
        address_book[full_name]= address
        x = input("Do you want to continue Y/N?").lower()


gather_info('Hello')
for name, address in address_book.items():
    print(f'{name.title()} at {address.title()}')




# if user adds informaion ask for them to do it again

# true/false user quits

# elif false(quit) 

# user quits - end loop

# print(fomatted diction)

# def name_address


