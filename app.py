import os

# BAD: Hardcoded password
password = "admin123"

# BAD: Command injection
filename = input("Enter file name: ")
os.system("cat " + filename)
