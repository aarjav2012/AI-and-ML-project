def time_converter():
    print("\nTime Conversion:")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    print("3. Minutes to Hours")
    print("4. Hours to Minutes")
    print("5. Hours to Days")
    print("6. Days to Hours")

    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value / 60, "minutes")
    elif choice == 2:
        print("Result:", value * 60, "seconds")
    elif choice == 3:
        print("Result:", value / 60, "hours")
    elif choice == 4:
        print("Result:", value * 60, "minutes")
    elif choice == 5:
        print("Result:", value / 24, "days")
    elif choice == 6:
        print("Result:", value * 24, "hours")
    else:
        print("Invalid choice")