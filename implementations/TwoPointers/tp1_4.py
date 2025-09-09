"""
Find all pairs with target sum
"""


def find_all_pairs_target(arr: list[int], target: int) -> list[int]:
    left, right = 0, len(arr) - 1
    res = []

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            res.append([left, right])
            left += 1
        elif curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1

    return res


print(find_all_pairs_target([1, 2, 2, 3, 4], 7))
