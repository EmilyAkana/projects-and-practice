"""Login program to check  information"""

user_information = []

name = input("Enter your name, please: ").lower().rstrip().lstrip()
user_information.append(name)

print(f"So, your name is {name.capitalize()}, thank you!\n")

age = int(input("Enter your current age: "))
user_information.append(age)

try:
    if age < 18:
        print("You aren't allowed into the website!")
    else:
        print(f"Your age is {age}, a few questions more and you can access!")
except ValueError:
    print(f"{age}, isn't age really")
