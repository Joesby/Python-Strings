#Task 1: Input Length Validator
first_and_last = input("What is your first and last name? ")

name_list = first_and_last.split()
first_name = name_list[0].capitalize()
last_name = name_list[1].capitalize()

if len(first_name) < 2 or len(last_name) < 2:
    print("Error: please don't use initials.")
else:
    print(first_name + " " + last_name + " is a wonderful name!")