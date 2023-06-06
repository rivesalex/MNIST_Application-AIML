import numpy as np

# Create a function that finds the center of mass / midpoint of any grid:

def get_midpoint(A):
    matrix_total = sum(A)
    x_total = 0
    y_total = 0

    n_columns = len(A[0,:])
    for i in range(n_columns):
        x_total += sum(A[:,i])*i
        continue
    x_midpoint = round(x_total/matrix_total)
    
    n_rows = len(A[:,0])
    for i in range(n_rows):
        y_total += sum(A[i,:])*i
        continue
    y_midpoint = round(y_total/matrix_total)

    return (x_midpoint,y_midpoint)

# Given two number midpoints: create a new matrix that allows them to be combined

def combine_numbers(N1,N2):
    x_n1,y_n1 = get_midpoint(N1)
    x_n2,y_n2 = get_midpoint(N2)

    # We want to offset the midpoints so that the horizontal distance is 7
    # We want to offset the midpoints so that the vertical distance is 0

    