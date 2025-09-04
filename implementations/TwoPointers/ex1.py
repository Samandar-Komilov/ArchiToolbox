"""
Pair with Target Sum: Given a sorted array, find if there exists a pair with sum = target
"""

arr = [3, 2, 4]
target = 6

left, right = 0, len(arr) - 1

while left < right:
    curr_sum = arr[left] + arr[right]

    if curr_sum == target:
        print(f"arr[{left}] and arr[{right}].")
        break
    elif curr_sum < target:
        left += 1
    else:
        right -= 1
    
