def days_to_units(no_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{no_of_days} days are {no_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{no_of_days} days are {no_of_days * 24 * 60} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{no_of_days} days are {no_of_days * 24 * 60 * 60} {conversion_unit}"
    else:
        return f"unsupported unit"
    

# here "days_and_units_dictionary" variable is defined in main.py
# But the helper.py file uses this variable
# Inorder to pass this varible to helper.py file 
# we need to pass this variable as argument to "validate_and_execute()" function 

def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_num = int(days_and_units_dictionary["days"])
        if user_input_num > 0:    
            calculated_value = days_to_units(user_input_num, days_and_units_dictionary["units"])
            print(calculated_value)
        elif user_input_num == 0:
            print("You entered a 0, Please enter a valid positive number")
        else:
            print("You entered a negative number, no converstation for you")
    except ValueError:
        print("your input is not a number.")


user_input_message = "Hey user enter the no of days and conversition unit:\n"