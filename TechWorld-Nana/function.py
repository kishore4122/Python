# Functions are mainly used to avoid repeating the same logic

calculation_to_hours = 24 
name_of_unit = "hours"


def days_to_units(no_of_days, custom_message):
    print(f"{no_of_days} days are {no_of_days * calculation_to_hours} {name_of_unit}")
    print(custom_message)



days_to_units(20, "cool")
days_to_units(35, "Awsome!")
