from helper import * #here "*" means we are importing everything (all functions and variables) from "helper" module

# from helper import validate_and_execute, user_input_message
# here we are importing only "validate_and_execute()" function and "user_input_message" variable from "helper" module

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    validate_and_execute(days_and_units_dictionary)

# here days_and_units_dictionary variable is defined in main.py
# But the helper.py file uses this variable
# inorder to pass this varible to helper.py file 
# we need to pass this variable as argument to "validate_and_execute()" function