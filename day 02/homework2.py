def double_age_check():
    age = int(input("Enter the current age: "))
    doubled_age = age * 2
    print(f"Doubled age: {doubled_age}")
    if doubled_age >= 30:
        print("Doubled age is greater than or equal to 30.")
    else:
        print("Doubled age is less than 30.")

double_age_check()
