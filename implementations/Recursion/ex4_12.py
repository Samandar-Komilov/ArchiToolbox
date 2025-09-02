"""
Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction.
"""


def product(m: int, n: int) -> int:
    if m == 0:
        return 0
    if m == 1:
        return n

    return n + product(m - 1, n)


print(product(5, 6))
