"""
Segregate Even and Odd numbers
"""


def segregate(arr: list[int]) -> list[int]:
    lp, rp = 0, len(arr) - 1

    while lp < rp:
        if arr[lp] % 2 == 1:
            tmp = arr[rp]
            arr[rp] = arr[lp]
            arr[lp] = tmp
            lp += 1
            while arr[rp] % 2 == 1:
                rp -= 1
        else:
            lp += 1

    return arr


print(segregate([1, 2, 3, 4, 5, 6]))
