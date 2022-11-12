import helper as h

user_input = ""
while user_input != "exit":
    user_input = input(h.user_input_message) # "user_input_message" is a variable declared in helper.py. so we mention the module alias name "h" 
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    h.validate_and_execute(days_and_units_dictionary)   # "validate_and_execute()" is a function declared in helper.py. so we mention the module alias name "h"

# here days_and_units_dictionary variable is defined in main.py
# But the helper.py file uses this variable
# inorder to pass this varible to helper.py file 
# we need to pass this variable as argument to "validate_and_execute()" function