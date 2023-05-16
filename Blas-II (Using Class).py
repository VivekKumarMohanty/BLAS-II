import numpy as np

class BLAS_2_single:
    
    def __init__(self, rows, cols, alpha, A):

            self.rows = rows
            self.cols = cols
            self.alpha = alpha
            self.A = A
            
    def matrix_vector(self):
        
        matrix_a = [] # Initialize matrix
        print("Enter the Entries:")

        for i in range(self.rows):
            a =[]
            for j in range(self.cols):      
                a.append(int(input()))
            matrix_a.append(a)

        for i in range(self.rows):
            for j in range(self.cols):
                print(matrix_a[i][j], end=" ")
            print()

        print("Matrix A = \n",matrix_a)

        vector_size = int(input("enter size of vector: "))
        vector=[]
        print("enter entries")
        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res = np.dot(matrix_a, vector)

        print(" --------- Matrix multiplication: ------------ ")
        print("The Result: ")
        print(final_res)
        
    def symmetric_matrix_vector(self):
        print("----------------------------------------------------")
        print("SYMMETRIC MATRIX VECTOR MULTIPLY")
        print("----------------------------------------------------")

        matrix_sym_a = []

        no_of_rows = int(input("Enter the number of rows:"))
        no_of_col = int(input("Enter the number of columns:"))

        print("Enter the Entries:")

        for i in range(no_of_rows):         
            a =[]
            for j in range(no_of_col):      
                a.append(int(input()))
            matrix_sym_a.append(a)

        for i in range(no_of_rows):
            for j in range(no_of_col):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n",matrix_sym_a)

        def symmetric(row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if(i < j or i >j):
                        matrix_sym_a[i][j] = matrix_sym_a[j][i]
                
        print("Symmetric Matrix: ")
        symmetric(no_of_rows, no_of_col)
        for i in range(no_of_rows):
            for j in range(no_of_col):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n",matrix_sym_a)

        vector_size = int(input("enter size of vector"))
        vector=[]
        print("enter entries for vector:")

        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_sym_res = np.dot(matrix_sym_a, vector)

        print("\nMatrix multiplication: ")
        print("The Result")
        print(final_sym_res)
        
    def triangular_matrix_vector(self):
        print("------------------------------------------")
        print("TRAINGULAR MATRIX VECTOR MULTIPLY")
        print("------------------------------------------")

        matrix_sym_a = []

        no_of_rows = int(input("Enter the number of rows:"))
        no_of_col = int(input("Enter the number of columns:"))

        print("Enter the Entries:")

        for i in range(no_of_rows):
            a = []
            for j in range(no_of_col):
                a.append(int(input()))
            matrix_sym_a.append(a)

        for i in range(no_of_rows):
            for j in range(no_of_col):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n", matrix_sym_a)

        def lower(matrix, row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if (i < j):
                        print("0", end=" ")
                        matrix_sym_a[i][j] = (0)
                    else:
                        print(matrix[i][j],end=" ")
                        matrix_sym_a[i][j] = matrix[i][j]
                print(" ")
                
        print("Triangular matrix: ")
        lower(matrix_sym_a, no_of_rows, no_of_col)
        print(matrix_sym_a)

        vector_size = int(input("enter size of vector"))
        vector=[]
        print("enter entries vector entries: ")

        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res = np.dot(matrix_sym_a, vector)

        print("The Result: ")
        print(final_res)
        
    def triangular_banded_matrix_vector(self):
        print("------------------------------------------")
        print("TRIANGULAR BANDED MATRIX MULTIPLICATION")
        print("------------------------------------------")

        #============== MATRIX A ================

        matrix_sym_a = []

        no_of_rows = int(input("Enter the number of rows:"))
        no_of_col = int(input("Enter the number of columns:"))

        print("Enter the Entries:")

        for i in range(no_of_rows):
            a = []
            for j in range(no_of_col):
                a.append(int(input()))
            matrix_sym_a.append(a)

        for i in range(no_of_rows):
            for j in range(no_of_col):
                print(matrix_sym_a[i][j], end=" ")
            print()
        print("Matrix A = \n", matrix_sym_a)

        k = 1
        def lower(matrix, row, col):
            for i in range(0, row):
                for j in range(0, col):
                    if (i < j):
                        print("0", end=" ")
                        matrix_sym_a[i][j] = (0)
                    else:
                        print(matrix[i][j],end=" ")
                        matrix_sym_a[i][j] = matrix[i][j]
                        
                        if i-j>k:
                            matrix_sym_a[i][j] = 0
                print(" ")

        print("Triangular matrix: ")
        lower(matrix_sym_a, no_of_rows, no_of_col)
        print(matrix_sym_a)

        vector_size = int(input("enter size of vector"))
        vector=[]
        print("enter entries vector entries: ")

        for i in range(vector_size):
            vector.append(int(input()))
        print("vector: ", vector)

        final_res = np.dot(matrix_sym_a, vector)

        print("The Result: ")
        print(final_res)
        
rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of columns:"))
alpha = int(input("Enter the value of alpha:"))
A = int(input("Enter the value of A:"))

single = BLAS_2_single(rows, cols, alpha, A)
single.matrix_vector()