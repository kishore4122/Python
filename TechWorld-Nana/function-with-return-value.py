calculation_to_hours = 24   #Global scope variables that means they can be used in any function
name_of_unit = "hours"


def days_to_units(no_of_days):
    return f"{no_of_days} days are {no_of_days * calculation_to_hours} {name_of_unit}"
    

my_var = days_to_units(110)
print(my_var)

