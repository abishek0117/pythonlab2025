# pythonlab2025

1. Base Conversion


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



2. Operators


# Input: 10 and 3

a = int(input("Enter first number: "))    # Output: 10
b = int(input("Enter second number: "))   # Output: 3

print("Addition:", a + b)                 # Output: 13
print("Logical AND:", a > 5 and b < 10)   # Output: True
print("Bitwise OR:", a | b)               # Output: 11



3. if, for, while, match-case


# Input: 404

x = int(input("Enter a number: "))        # Output: 404

if x > 0:
    print("Positive")                     # Output: Positive

for i in range(3):
    print("For loop:", i)                 # Output: 0,1,2

i = 0
while i < 2:
    print("While loop:", i)               # Output: 0,1
    i += 1

def http_code(status):
    match status:
        case 404:
            return "Not Found"
        case _:
            return "Unknown"

print("Match-case:", http_code(x))        # Output: Not Found


4. Array Operations


# Input: 4 8 1 9

arr = list(map(int, input("Enter array elements: ").split()))  # [4, 8, 1, 9]
print("Sum:", sum(arr))        # Output: 22
print("Max:", max(arr))        # Output: 9
print("Min:", min(arr))        # Output: 1
print("Sorted:", sorted(arr))  # Output: [1, 4, 8, 9]


5. String Operations


# Input: Hello World

s = input("Enter a string: ")         # Hello World
print("Uppercase:", s.upper())        # HELLO WORLD
print("Lowercase:", s.lower())        # hello world
print("Length:", len(s))              # 11
print("Reversed:", s[::-1])           # dlroW olleH


6. Bank Account


# Sample Run:
# Deposit: 1000
# Withdraw: 500

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amt):
        self.balance += amt
        print("Deposited:", amt)

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount("John")
acc.deposit(1000)            # Deposited: 1000
acc.withdraw(500)            # Withdrawn: 500
acc.show_balance()           # Balance: 500


7. Recursive Factorial

# Input: 5

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter number: "))      # 5
print("Factorial:", factorial(n))     # Output: 120

8. Lambda Function


nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print("Squared:", squared)           # Output: [1, 4, 9, 16]

9. File Operations

import os

with open("file.txt", "w") as f:
    f.write("Hello")

with open("file.txt", "r") as f:
    print("Read:", f.read())         # Output: Hello

with open("file.txt", "a") as f:
    f.write("\nWorld")

os.rename("file.txt", "renamed.txt")  # File renamed to renamed.txt

10. List Operations

lst = []
lst.append("apple")
lst.append("banana")
print("List:", lst)             # ['apple', 'banana']
lst.remove("apple")
print("After remove:", lst)     # ['banana']

11. Prime Check


# Input: 7

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))       # 7
print("Prime?" , is_prime(num))          # Output: True


12. Class with Attributes

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s = Student("Anjali", 101)
s.display()
# Output:
# Name: Anjali
# Roll: 101


