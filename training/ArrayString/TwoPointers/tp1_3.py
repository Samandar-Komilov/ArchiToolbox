"""
Pair Sum Exists
"""


def pair_sum_exists(arr: list[int], target: int) -> bool:
    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return True
        elif curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1

    return False


print(pair_sum_exists([1, 2, 4, 7, 11, 15], 16))
print(pair_sum_exists([1, 2, 4, 7, 11, 15], 23))
