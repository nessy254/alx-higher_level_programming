#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        print(" ".join("{:d}".format(m) for m in mat))


