#string concatenation

print("20 days are " + str(50) + "minutes") #old
print(f"20 days are {50 * 24 * 60} minutes") #new


#functions in python
calculation_to_units = 24
name_of_units = "hours"

def days_to_units():
    print(f"20 days are {20 * calculation_to_units} {name_of_units}")
    print("no error has been detacted!")

days_to_units()


#smartest writing of python codes
calculation_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {20 * calculation_to_units} {name_of_units}")

days_to_units(20)
days_to_units(35)
days_to_units(20)
days_to_units(50)
days_to_units(110)
