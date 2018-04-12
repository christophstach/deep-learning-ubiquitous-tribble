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
            row.append(randint(0,255))
        mat.append(row)
    
    return mat

def matrix_vector_mul(mat, vec):
    return []

def matrix_transpose(a):
    return []
