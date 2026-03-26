def weight_converter():
    print("\nWeight Conversion:")
    print("1. Kg to Gram")
    print("2. Gram to Kg")

    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value * 1000, "g")
    elif choice == 2:
        print("Result:", value / 1000, "kg")
    else:
        print("Invalid choice")