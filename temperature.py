def temperature_converter():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        result = (value * 9/5) + 32
        print("Result:", result, "°F")
    elif choice == 2:
        result = (value - 32) * 5/9
        print("Result:", result, "°C")
    else:
        print("Invalid choice")