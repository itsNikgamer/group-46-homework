def generate_even_numbers():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    print("Even numbers in the range:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print()  # Newline for clean output

generate_even_numbers()