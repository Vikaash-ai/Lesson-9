age = int(input("Please enter your grade: "))

if age > 10:
    print("You are grader than 10!")
    if age < 20:
        print("You are less than 20!")
        print("You are enrolled")
    else:
        print("You are too old or young to enrol to class.")
else:
    print("Invalid input")