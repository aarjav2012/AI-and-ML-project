def length_converter():
    print("\nLength Conversion:")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Meter to Centimeter")
    print("4. Centimeter to Meter")

    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value / 1000, "km")
    elif choice == 2:
        print("Result:", value * 1000, "m")
    elif choice == 3:
        print("Result:", value * 100, "cm")
    elif choice == 4:
        print("Result:", value / 100, "m")
    else:
        print("Invalid choice")