#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    """Triangle"""
    if n <= 0:
        return []
    pas_tri = [[1]]
    for row_number in range(1, n):
        row = [1]
        for j in range(1, row_number):
            element = pas_tri[row_number - 1][j - 1] + pas_tri[row_number - 1][j]
            row.append(element)
        row.append(1)
        pas_tri.append(row)

    return pas_tri
