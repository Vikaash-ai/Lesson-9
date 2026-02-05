medicine_cause = str(input("Do you have any Medicine Cause Y or N?: "))

attendence = int(input("Please enter the students attendence: "))

if medicine_cause == 'Y':
    print("You are allowed to do the exam!")
else:
    if attendence >= 75:
        print(f"You are alowed to do the exam because you have a attendence of {attendence}!")
    else:
        print("SORRY YOU CANNOT DO THE EXAM")