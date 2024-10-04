#!/usr/bin/python3
"""This moodule defines the function pascal_triangle which
prints a pascal triangle
"""


def pascal_triangle(n):
    """ This function returns a list of integers representing the
        Pascal's triangle of n.
    """
    pascal_triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0:
                row.append(1)
                continue
            else:
                leftupper = (
                    0 if i-1 < 0 or j-1 < 0 else
                    pascal_triangle[i - 1][j - 1]
                )
                rightupper = (
                    0 if i-1 < 0 or j >= len(pascal_triangle[i - 1]) else
                    pascal_triangle[i - 1][j]
                    )
                row.append(leftupper + rightupper)
        pascal_triangle.append(row)
    return (pascal_triangle)
