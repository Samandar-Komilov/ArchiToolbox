"""
Intersection of two sorted arrays
"""


def intersection_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    res = []
    rp1, rp2 = 0, 0

    while rp1 < len(arr1) and rp2 < len(arr2):
        if arr1[rp1] == arr2[rp2]:
            res.append(arr1[rp1])
            rp1 += 1
            rp2 += 1
        elif arr1[rp1] < arr2[rp2]:
            rp1 += 1
        elif arr2[rp2] < arr1[rp1]:
            rp2 += 1

    return res


print(intersection_arrays([1, 2, 2, 3, 5], [2, 2, 4, 5, 8, 9, 10]))
