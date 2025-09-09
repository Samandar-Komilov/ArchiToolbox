"""
Merge two sorted arrays (like merge step in merge sort)
"""


def merge_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    res = [0] * (len(arr1) + len(arr2))
    rp1, rp2, wp = 0, 0, 0

    while rp1 < len(arr1) and rp2 < len(arr2):
        if arr1[rp1] < arr2[rp2]:
            res[wp] = arr1[rp1]
            rp1 += 1
        else:
            res[wp] = arr2[rp2]
            rp2 += 1

        wp += 1

    # When len(arr2) < len(arr1)
    while rp1 < len(arr1):
        res[wp] = arr1[rp1]
        rp1 += 1
        wp += 1

    # when len(arr2) > len(arr1)
    while rp2 < len(arr2):
        res[wp] = arr2[rp2]
        rp2 += 1
        wp += 1

    return res


print(merge_arrays([1, 3, 5], [2, 4, 6]))
