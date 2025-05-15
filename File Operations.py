import os

with open("file.txt", "w") as f:
    f.write("Hello")

with open("file.txt", "r") as f:
    print("Read:", f.read())         # Output: Hello

with open("file.txt", "a") as f:
    f.write("\nWorld")

os.rename("file.txt", "renamed.txt")  # File renamed to renamed.txt

