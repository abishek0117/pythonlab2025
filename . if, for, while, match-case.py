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
