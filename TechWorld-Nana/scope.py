calculation_to_hours = 24   #Global scope variables that means they can be used in any function
name_of_unit = "hours"


def days_to_units(no_of_days, custom_message):
    print(f"{no_of_days} days are {no_of_days * calculation_to_hours} {name_of_unit}")
    print(custom_message)

def scope_check(num_of_days):
    my_var = "variable inside function" #Local scope variables that means they can be used inside funtion
    print(name_of_unit) #varible from the Global Scope
    print(num_of_days) 
    print(my_var)

days_to_units(110, "kishroe")
scope_check(20)

