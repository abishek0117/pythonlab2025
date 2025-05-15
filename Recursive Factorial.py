# Input: 5

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter number: "))      # 5
print("Factorial:", factorial(n))     # Output: 120
