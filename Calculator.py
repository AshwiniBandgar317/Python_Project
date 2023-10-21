while True:
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))

    print("Select Operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == 2:
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == 3:
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == 4:
        print(num1, "/", num2, "=", num1 / num2)

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break



