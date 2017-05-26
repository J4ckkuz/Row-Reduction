##################
# Elementary row operations:
# Multiplying a row by a constant
# Switching rows
# Adding a row to another row (and often multiplying by a constant)

# Matrix format: a two-dimensional array. 
# Need to specify whether matrix is augmented or not
augmentedMatrix = [ [1, 2, -3, 0], [-4, 2, 1, 2], [3, 8, -1, 15] ]
matrixA = [ [1, 3, 2], [2, 0, 1], [5, 2, 2] ]
matrixB = [4, 3, 1]

def augmentMatrix(matrixA, matrixB):
    """The first argument is the matrix of coefficients, and the second is the matrix of constants."""

    assert len(a) == len(b), "Both matrices must have the same number of rows."
    i = 0
    for row in a:
        row.append(b[i])
        i += 1
    return a

def multiplyRow(matrix, row, constant):
    """Multiply only one row of a matrix by a constant. Zero-based."""

    m = list(matrix) # copies the list, rather than passing it by reference
    m[row] = [ x * constant for x in m[row] ]
    # m[row] = list(map(lambda x: x * constant, m[row])) # this also works, but is less clear.
    return m

def switchRows(matrix, rowA, rowB):
    m = list(matrix)
    m[rowA], m[rowB] = m[rowB], m[rowA]
    return m

def addRows( matrix, a, b, constant=1 ):
    """Adds a to b, where a and b are rows.
    b = b + a * constant
    constant can be left blank. default value: 1"""
    
    if constant is None:
        constant = 1

    m = list(matrix)
    m[b] = [m[b][i] + (m[a][i] * constant) for i in range(len(m[b]))]
    return m

print( addRows( augmentedMatrix, 0, 1, 5) )