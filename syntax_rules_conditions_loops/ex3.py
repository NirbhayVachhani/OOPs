while True: #loop starts 
    print("\nSimple Calculator")
    print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 0. Exit \n")

    menu_option = int(input("Enter menu option: ")) # to select option 

    if menu_option == 0: #condition check for 0
        print("Calculator app closed")
        break # loop breaks if 0 is entered in menu_option

    first_number = float(input("Enter the first number: ")) #enter 1st number
    second_number = float(input("Enter the second number: ")) #enter 2nd number 

    if menu_option == 1: #condition check for 1
        print(first_number, "+", second_number, "=", first_number + second_number)
    elif menu_option == 2: #condition check for 2
        print(first_number, "-", second_number, "=", first_number - second_number)
    elif menu_option == 3: #condition check for 3
        print(first_number, "*", second_number, "=", first_number * second_number)
    elif menu_option == 4: #condition check for 4
        if second_number == 0: #condition check if number is 0
            print("Cannot divide by 0")
        else:
            print(first_number, "/", second_number, "=", first_number / second_number)
    else:
        print("Invalid option/number")
