# Validate user input
# We want to avoid or handle values:
#   which does not make sense, that could crash our program, could even be a security risk    


calculation_to_hours = 24   #Global scope variables that means they can be used in any function
name_of_unit = "hours"


def days_to_units(no_of_days):
        return f"{no_of_days} days are {no_of_days * calculation_to_hours} {name_of_unit}"
    
   
def validate_and_execute():
    if user_input.isdigit():
        # Converting entered input into integer
        user_input_num = int(user_input)
        if user_input_num > 0:    
            # Calling function with user input and saving result into a variable
            calculated_value = days_to_units(user_input_num)
            # calculated_value = days_to_units(int(user_input))
            #Printing the result which was saved in a variable
            print(calculated_value)
        elif user_input_num == 0:
            print("You entered a 0, Please enter a valid positive number")
    else:
        print("your input is not a number.")

# Ask for user input
user_input = input("Hey user enter the no of days, i converted it into hours:\n")
validate_and_execute()

