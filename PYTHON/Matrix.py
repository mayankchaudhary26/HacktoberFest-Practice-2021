# Input two values m and n, and create a matrix m x n

matrix = [] # Variable to matrix
m = int(input()) # Row of matrix
n = int(input()) # Column of matrix

def create_matrix(m, n, matrix): # Function to create a matrix
    for l in range(1, m + 1): # loop for the row
        line = []
        for c in range(1, n + 1): # loop for the column
            x = int(input('%i%i '%(l, c))) # input of the values of row 'nd column
            line.append(x)
        matrix.append(line)

create_matrix(m, n, matrix) # Call the function

print(matrix) # Print the matrix
