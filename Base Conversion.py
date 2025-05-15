
# Input
# Enter the input base (e.g., 2, 8, 10, 16): 10
# Enter the number to be converted: 15

input_base = int(input("Enter the input base (e.g., 2, 8, 10, 16): "))
input_number = input("Enter the number to be converted: ")

if input_base == 10:
    num = int(input_number)
    print("Binary:", bin(num)[2:])        # Output: Binary: 1111
    print("Octal:", oct(num)[2:])         # Output: Octal: 17
    print("Hexadecimal:", hex(num)[2:].upper())  # Output: Hexadecimal: F

