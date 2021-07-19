#function execution in python
#user_input
calculation_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")

    user_input = input("hello can you enter something!\n")
    print(user_input)

calculation_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"

my_var = days_to_units(20)
print(my_var)

#coditional statement
calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    else:
        return "you in  wrong channel, for the codes."
user_input = input("hello am a convertor, can help you make your convetion easy!\n")
user_input_number = int(user_input)

calculated_value_number = days_to_units(user_input_number)
print(calculated_value_number)

#more users input validation
