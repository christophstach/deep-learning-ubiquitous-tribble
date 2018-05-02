from random import randint
""" Some functions for basic linear algebra opertations based on python lists. """


def vector_add(a, b):
    result = []

    for index in range(len(a)):
        result.append(a[index] + b[index])

    return result


def vector_sub(a, b):
    result = []

    for index in range(len(a)):
        result.append(a[index] - b[index])

    return result

def vector_scalar_mul(r, a):
    result = []

    for i in a:
        result.append(i * r)

    return result


def vector_dot(a, b):
    result = 0
    
    for index in range(len(a)):
        result += a[index] * b[index]
        
    return result

def create_random_matrix(n, m):
    mat = []
    
    for i in range(n):
        row = []
        for i in range(m):
            row.append(randint(0, 255))
        mat.append(row)
    
    return mat

def matrix_vector_mul(mat, vec):
    result = []
    
    for rowIndex, rowValue in enumerate(mat):
        result.append(0)
        for colIndex, colValue in enumerate(rowValue):
            result[rowIndex] += colValue * vec[colIndex]
    
    return result

def matrix_transpose(a):
    result = []

    cols = len(a)
    rows = len(a[0])

    for r in range(rows):
        result.append([])
        for c in range(cols):
            result[r].append(a[c][r])
            
   
    return result
