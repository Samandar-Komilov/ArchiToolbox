"""
Move All Zeroes to End
"""


def move_zeroes(arr: list[int]) -> list[int]:
    lp, rp = 0, len(arr) - 1

    while lp < rp:
        if arr[lp] == 0:
            tmp = arr[rp]
            arr[rp] = arr[lp]
            arr[lp] = tmp
            lp += 1
            rp -= 1
        else:
            lp += 1

    return arr


print(move_zeroes([0, 1, 0, 3, 6]))
