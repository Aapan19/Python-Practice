# Validate User input Exercise
# 1. Username is not more then 12 characters.
# 2. Username must not contain spaces
# 3. Username must not contain digit


username = input("Enter your User name: ")


if len(username)>12:
    print("Your Username can't more then 12 characters")
elif not username.find(" ") == -1:
    print("Your Username can't contain space")
elif not username.isalpha():
    print("Your Username can't contain Numbers")
else:
    print(f"Welcome {username}")