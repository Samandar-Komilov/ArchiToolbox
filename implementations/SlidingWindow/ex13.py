"""
- Max consecutive ones after flipping k zeros (simplified)
"""

nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
k = int(input("Enter k: "))
max_len = 0

win_start, zero_count = 0, 0

for win_end in range(len(nums)):
    if nums[win_end] == 0:
        zero_count += 1
        print("Encountered 0, zc++")
    if zero_count <= k:
        max_len = max(max_len, win_end - win_start + 1)
        print(f"0s are not > k yet, update maxlen = {max_len}")

    while zero_count > k:
        print(f"0s > k, shrink by removing nums[{win_start}] = {nums[win_start]}")
        if nums[win_start] == 0:
            zero_count -= 1
        win_start += 1

print(max_len)
