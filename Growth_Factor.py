# The Gorwth Factor Program can be used to figure out how much the value of something has increased or decreased by.

increase_or_decrease = input("Do you want to use this program to increase or decrease the value? ").lower()
percentage_factor = input("Enter a percentage_factor: ")
growth_factor_for_addition = 1 + percentage_factor

if increase_or_decrease == "increase" and percentage_factor.isdigit():
    growth_factor_for_addition = int(growth_factor_for_addition)
    print(percentage_factor)