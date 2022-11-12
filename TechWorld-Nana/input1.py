calculation_to_hours = 24   #Global scope variables that means they can be used in any function
name_of_unit = "hours"


def days_to_units(no_of_days):
    return f"{no_of_days} days are {no_of_days * calculation_to_hours} {name_of_unit}"

# Ask for user input
user_input = input("Hey user enter the no of days, i converted it into hours:\n")

# Converting entered input into integer
user_input_num = int(user_input)

# Calling function with user input and saving result into a variable
calculated_value = days_to_units(user_input_num)

#Printing the result which was saved in a variable
print(calculated_value)