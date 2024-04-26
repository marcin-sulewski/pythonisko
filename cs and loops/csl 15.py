import re

password = input("Enter a password: ")

if 6 <= len(password) <= 16:
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        if re.search("[0-9]", password):
            if re.search("[$#@]", password):
                print("Valid password")
                exit()
print("Invalid password")
