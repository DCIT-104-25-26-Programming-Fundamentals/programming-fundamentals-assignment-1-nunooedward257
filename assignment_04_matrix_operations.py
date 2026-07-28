# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix():
    # Read an M x N matrix from the user.
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows <= 0 or cols <= 0:
                print("Error: Rows and columns must be positive integers.")
                continue
            break
        except ValueError:
            print("Error: Please enter valid integers for rows and columns.")

    matrix = []
    for row_index in range(rows):
        while True:
            try:
                row_values = input(f"Enter row {row_index + 1}: ").split()
                if len(row_values) != cols:
                    print(f"Error: Row {row_index + 1} must contain {cols} values.")
                    continue

                values = []
                for value in row_values:
                    values.append(int(value))

                matrix.append(values)
                break
            except ValueError:
                print("Error: Please enter only integers.")

    return matrix

# Print a matrix in a neat, aligned grid format.
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:>6}", end="")
        print()

# Return the transpose of a matrix using nested loops.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    transpose = []
    for col_index in range(cols):
        new_row = []
        for row_index in range(rows):
            new_row.append(matrix[row_index][col_index])
        transpose.append(new_row)

    return transpose 

# Return the element-wise sum of two matrices.
def add_matrices(matrix_a, matrix_b):
    result = []
    for row_index in range(len(matrix_a)):
        new_row = []
        for col_index in range(len(matrix_a[0])):
            new_row.append(matrix_a[row_index][col_index] + matrix_b[row_index][col_index])
        result.append(new_row)
    return result


# Return the product of two matrices using nested loops.
def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0

    if cols_a != rows_b:
        return None

    result = []
    for row_index in range(rows_a):
        new_row = []
        for col_index in range(cols_b):
            total = 0
            for inner_index in range(cols_a):
                total += matrix_a[row_index][inner_index] * matrix_b[inner_index][col_index]
            new_row.append(total)
        result.append(new_row)

    return result


# Perform Part A: transpose a matrix.
def part_a_transpose():
    print("\nPart A — Transpose a Matrix")
    matrix = read_matrix()

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transposed)


# Perform Part B: add two matrices.
def part_b_addition():
    print("\nPart B — Add Two Matrices")
    print("Enter matrix A:")
    matrix_a = read_matrix()
    print("\nEnter matrix B:")
    matrix_b = read_matrix()

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("Error: Both matrices must have the same dimensions.")
        return

    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)

    result = add_matrices(matrix_a, matrix_b)
    print("\nSum Matrix:")
    display_matrix(result)


# Perform Part C: multiply two matrices.
def part_c_multiplication():
    print("\nPart C — Multiply Two Matrices")
    print("Enter matrix A:")
    matrix_a = read_matrix()
    print("\nEnter matrix B:")
    matrix_b = read_matrix()

    if len(matrix_a[0]) != len(matrix_b):
        print("Error: The number of columns in matrix A must equal the number of rows in matrix B.")
        return

    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)

    result = multiply_matrices(matrix_a, matrix_b)
    if result is None:
        print("Error: Matrix multiplication is not possible with these dimensions.")
    else:
        print("\nProduct Matrix:")
        display_matrix(result)


def main():
    while True:
        print("\nMatrix Operations Menu")
        print("1. Transpose a matrix")
        print("2. Add two matrices")
        print("3. Multiply two matrices")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            part_a_transpose()
        elif choice == "2":
            part_b_addition()
        elif choice == "3":
            part_c_multiplication()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

