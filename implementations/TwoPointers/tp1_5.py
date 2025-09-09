"""
Container with most water
"""


def container_with_most_water(arr: list[int]):
    left, right = 0, len(arr) - 1
    maxvol = 0

    while left < right:
        currvol = (right - left) * min(arr[left], arr[right])
        maxvol = max(maxvol, currvol)
        print(currvol, maxvol, left, right)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return maxvol


print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 4]))
