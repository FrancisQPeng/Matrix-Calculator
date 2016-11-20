## Matrix Calulator.
## Below are functions for m x n matrices, represented by 2D lists.
## Functionalities include:
##  - inverse matrix
##  - adjugate matrix
##  - determinant of matrix
##  - cofactor expansion
##  - transpose of matrix
##  - dot product
##  - matrix multiplication
##  - basis of matrix
## The point of this was to help me with 2D array manipulations and to better
##  understand the fundamentals of linear algebra and the simplex method


def invert_matrix(matrix):
    new_matrix = transpose_matrix(adjugate_matrix(matrix))
    
    n = len(matrix)
    det = find_determinant(matrix)
    
    if det == 0:
        return "This matrix is not invertible"
    else:
    
        for i in range(0,n):
            for j in range(0,n):
                new_matrix[i][j] = new_matrix[i][j] / det
            
        return new_matrix


def adjugate_matrix(matrix):
    new_matrix = []
    n = len(matrix)
    
    for i in range(0, n):
        row = []
        for j in range(0,n):
            if (i + j) % 2 == 0:
                counter = 1
            else:
                counter = -1
            row += [counter * find_determinant(cofactor_matrix(matrix, i,j))]
        new_matrix += [row]
    
    return new_matrix



def find_determinant(matrix):
    n = len(matrix)
    total_sum = 0
    
    if n == 1:
        return matrix[0][0]
    else:
        for i in range(0, n):
            if i % 2 == 0:
                counter = 1
            else:
                counter = -1
            total_sum += counter * matrix[0][i] * find_determinant(cofactor_matrix(matrix, 0, i))
        
    return total_sum
                                                             
                                                             
def cofactor_matrix(matrix, i, j):
    n = len(matrix)
    new_matrix = matrix[0:i] + matrix[i+1:n]
    for row_index in range(0,n-1):
        new_matrix[row_index] = new_matrix[row_index][0:j] + new_matrix[row_index][j+1:n]
    
    return new_matrix

def transpose_matrix(matrix):
    new_matrix = []
    n = len(matrix[0])
    m = len(matrix)
    
    for i in range(0, n):
        row = []
        for j in range(0,m):
            row += [matrix[j][i]]
        new_matrix += [row]
    
    return new_matrix

def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        print("Cannot dot product two vectors of different dimensions")
    else:
        n = len(vector1)
        sum = 0
        for i in range(0, n):
            sum += (vector1[i] * vector2[i])
        return sum
    
def matrix_multiply(left_matrix, right_matrix):
    if len(left_matrix[0]) != len(right_matrix):
        print ("Cannot multiply matrices of these dimensions")
    else:
        transpose = transpose_matrix(right_matrix)
        n = len(right_matrix[0])
        m = len(left_matrix)
        new_matrix = []
        for j in range(0,m):
            new_matrix.append([])
        for i in range(0, n):
            for j in range(0, m):
                new_matrix[j].append(dot_product(left_matrix[j], transpose[i]))
        return new_matrix
    
##Note: basis does not use index of 0, it will assume that first column is basis 1
def find_A_basis(constraint_matrix, basis):
    new_matrix = []
    for i in range(0, len(constraint_matrix)):
        row = []
        for index in basis:
            row += [constraint_matrix[i][index - 1]]
        new_matrix.append(row)
    return new_matrix
    

def create_identity(size):
    indexI = 0
    new_matrix = []
    for x in range(size):
        row = []
        index = 0
        for y in range(size):
            if (index == indexI):
                row.append(1)
            else:
                row.append(0)
            index += 1
        new_matrix.append(row)
        indexI += 1
    return new_matrix

def matrix_add_subtract(left_matrix, right_matrix, mode):
    new_matrix = []
    for row1, row2 in zip(left_matrix, right_matrix):
        print "row1: ", row1, "row2: ", row2
        new_row = []
        for item1, item2 in zip(row1, row2):
            if (mode == 'add'):
                new_item = item1 + item2
            elif(mode == 'sub'):
                new_item = item1 - item2
            new_row.append(new_item)
        new_matrix.append(new_row)
    return new_matrix
    
        
        
matrixA = [[1,2,3],[2,3,4],[1,0,5]]      
test_matrix = [[3,0,2],[2,0,-2],[0,1,1]]
test2 = [[1,2,3,4],[6,7,8,9],[2,3,2,1],[3,4,5,1]]
matrixB = [[1,2,3],[2,3,4],[1,0,5],[4,7,6]]
matrixC = [[1,2,3,6,7],[2,3,4,3,7],[1,0,5,9,1]]
inverse_matrixA = invert_matrix(matrixA)
identity = create_identity(3)




