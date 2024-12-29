def check_floor_division():
    num1 = float(input("Enter the first number (float): "))
    num2 = float(input("Enter the second number (float): "))
    if num2 != 0:
        result = num1 // num2
        print(f"The result of floor division {num1} // {num2} is {result}. It is always an integer.")
    else:
        print("Division by zero is undefined.")

check_floor_division()