calculation_to_hours = 24   
name_of_unit = "hours"


def days_to_units(no_of_days):
        return f"{no_of_days} days are {no_of_days * calculation_to_hours} {name_of_unit}"
    
   
def validate_and_execute():
    try:
        user_input_num = int(no_of_days_element)
        if user_input_num > 0:    
            calculated_value = days_to_units(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            print("You entered a 0, Please enter a valid positive number")
        else:
            print("You entered a negative number, no converstation for you")
    except ValueError:
        print("your input is not a number.")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user enter the no of days, i converted it into hours:\n")
    for no_of_days_element in set(user_input.split(",")): #here we convert the List into Set
        validate_and_execute()
