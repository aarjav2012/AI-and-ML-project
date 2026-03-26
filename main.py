from length import length_converter
from weight import weight_converter
from temperature import temperature_converter
from times import time_converter

while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Time")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        length_converter()
    elif choice == 2:
        weight_converter()
    elif choice == 3:
        temperature_converter()
    elif choice == 4:
        time_converter()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")

    end = input("\nDo you want to continue? (yes/no): ")
    if end == "yes":
        pass   
    else:
        print("thank you for using our program")
        break