def calculate_average():
    numbers = list(map(float, input("Enter numbers separated by commas (e.g., 2,2,2): ").split(',')))
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print(f"Sum of numbers: {total_sum}")
    print(f"Average of numbers: {average}")

calculate_average()