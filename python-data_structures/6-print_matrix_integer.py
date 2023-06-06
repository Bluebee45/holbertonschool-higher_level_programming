#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for l, t in enumerate(i):
            if l != len(i) - 1:
                print(t, end=" ")
            else:
                print("{:d}".format(t), end="")
        print()
