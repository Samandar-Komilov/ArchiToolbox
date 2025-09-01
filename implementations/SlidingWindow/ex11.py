"""
    - Longest Subarray with Sum <= k (positive integers)
"""

arr = [3, 1, 2, 7, 1, 1, 1, 1, 5]
k = int(input("Enter k: "))

curr_win_sum, max_len = 0, 0
win_start = 0


for win_end in range(len(arr)):
    curr_win_sum += arr[win_end]
    print(f"arr[{win_start}:{win_end+1}] sum = {curr_win_sum}")

    if (curr_win_sum <= k):
        max_len = max(max_len, win_end - win_start + 1)
        print(f"max_len = {max_len}")

    while (curr_win_sum > k):
        print(f"Shrinking by one: arr[{win_start}]")
        curr_win_sum -= arr[win_start]
        win_start+=1

print(max_len)