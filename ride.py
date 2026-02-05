print("Select a Vehicle: ")
print("1. Bike")
print("2. Car")
print("------------------------------------------------------")

choice = int(input("Please enter either 1 or 2 to select the vehicle: "))

if choice == 1:
    print("You chose the Bike")
    print("1. Scooty \n")
    print("2. Scooter \n")

    choice1 = int(input("Would you like 1 or 2 to select your bike: "))
    
    if choice1 == 1:
        print("You chose the Scooty")
    else:
        print("You chose the Scooter")
    
elif choice == 2:
    print("You chose the car")
    print("1. SEDAN")
    print("2. SUV")
    
    choice2 = int(input("Would you like 1 or 2 to select your car: "))
    
    if choice2 == 1:
        print("You chose the SEDAN")
    else:
        print("You chose the SUV")
        
else:
    print("You chose the wrong choice.")