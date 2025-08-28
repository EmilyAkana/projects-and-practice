"""Login program to check  information"""

user_information = []

name = input("Enter your name, please: ").lower().rstrip().lstrip()
user_information.append(name)

print(f"So, your name is {name.capitalize()}, thank you!\n")

age = int(input("Enter your current age: "))
user_information.append(age)

if age < 18:
    print("You aren't allowed into the website!\n")
else:
    print(f"Your age is {age}, a few questions more and you can access!\n")

terms = (
    input("Do you accept the terms and conditions? (Write yes or no): ")
    .lower()
    .lstrip()
    .rstrip()
)

if terms == "yes":
    terms = bool(True)
    user_information.append(terms)
    print("You accepted the terms and conditions of the service! :3")
else:
    terms = bool(False)
    user_information.append(terms)
    print("You didn't accepted the terms and conditions of the service.")
