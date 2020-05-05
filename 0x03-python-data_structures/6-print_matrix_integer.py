#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        num = 0
        if len(matrix[0]) == 0:
                print("")
        for row in matrix:
                count = 0
                for num in range(0, len(row)):
                        count += 1
                        if len(row) != count:
                                print("{:d}".format(row[num]), end=" ")
                        else:
                                print("{:d}".format(row[num]))
