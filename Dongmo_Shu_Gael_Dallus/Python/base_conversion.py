def convert_base(number, from_base, to_base):
    # Convert the number to decimal (base 10)
    decimal_number = int(str(number), from_base)
    
    # Convert the decimal number to the desired base
    converted_number = ""
    while decimal_number > 0:
        remainder = decimal_number % to_base
        converted_number = str(remainder) + converted_number
        decimal_number //= to_base
    
    return converted_number


# Get user input
number = input("Enter the number: ")
from_base = int(input("Enter the base of the number: "))
to_base = int(input("Enter the base to convert to: "))

# Convert the number to the desired base
converted_number = convert_base(number, from_base, to_base)

# Print the result
print(f"The converted number is: {converted_number}")