# =============================================================================
 # PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """Calculate the sum of numbers without using built-in sum()."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculate the average of numbers."""
    if len(numbers) == 0:
        return 0
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_maximum(numbers):
    """Find the maximum number without using built-in max()."""
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def calculate_minimum(numbers):
    """Find the minimum number without using built-in min()."""
    if len(numbers) == 0:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def main():
    """Main function to orchestrate the program."""
    # Get number count from user
    while True:
        try:
            n = int(input("How many numbers?: "))
            if n <= 0:
                print("Error: N must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid positive integer.")
    
    # Collect numbers from user
    numbers = []
    for i in range(1, n + 1):
        while True:
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Error: Please enter a valid number.")
    
    # Calculate statistics
    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_maximum(numbers)
    minimum = calculate_minimum(numbers)
    
    # Display results
    print("\nResults:")
    print(f"Sum:    {int(total)}")
    print(f"Average: {average}")
    print(f"Maximum: {int(maximum)}")
    print(f"Minimum: {int(minimum)}")


if __name__ == "__main__":
    main() 


