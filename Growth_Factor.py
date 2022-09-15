# The Growth Factor Program can be used to figure out how much the value of something has increased or decreased by.

increase_or_decrease = input("Do you want to use this program to increase or decrease the value? ").lower()

if increase_or_decrease == "increase":
    percentage_factor = input("Enter a percentage factor: ")
    percentage_factor = float(percentage_factor) # Converts the percentage factor inputed by the user to a decimal outside the string
    growth_factor = 1 + percentage_factor
    growth_factor_for_addition = float(growth_factor) # The reason that we are using 'float' instead of 'int', is that 'int' converts the number to a hole number, which means that it doesn't have decimals, and that is unprectical for this program
    old_value = input("Enter the old value: ")
    old_value = float(old_value)    
    new_value = old_value * growth_factor # Here we figure out what the new value is
    print(new_value)
elif increase_or_decrease == "decrease":
    percentage_factor = input("Enter a percentage factor: ")
    percentage_factor = float(percentage_factor)
    growth_factor = 1 - percentage_factor
    growth_factor = float(growth_factor)
    old_value = input("Enter the old value: ")
    old_value = float(old_value)    
    new_value = old_value * growth_factor
    print(new_value)
else:
    quit() # If the user types something other than 'increase' or 'decrease', the program will end