# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


# Prompt the user for a positive integer and validate the input.
def get_positive_integer(prompt):
    try:
        value = int(input(prompt))
    except ValueError:
        print("Error: Please enter a positive integer.")
        return None

    if value <= 0:
        print("Error: Please enter a positive integer.")
        return None

    return value


# Print the multiplication table for one number from 1 to 12.
def print_single_table(number):
    print(f"Multiplication Table for {number}:")
    for multiplier in range(1, 13):
        print(f"{number}  x  {multiplier:>2}  =  {number * multiplier}")


# Print multiplication tables for every number from 1 to n.
def print_tables_from_1_to_n(n):
    for number in range(1, n + 1):
        print_single_table(number)
        if number < n:
            print("-" * 27)


def main():
    number = get_positive_integer("Enter a number: ")
    if number is None:
        return

    print_single_table(number)

    n = get_positive_integer("Enter a number N for tables from 1 to N: ")
    if n is None:
        return

    print_tables_from_1_to_n(n)


if __name__ == "__main__":
    main()

