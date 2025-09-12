"""
- Sum of each window of size k
"""

arr = [1, 9, 8, 2, 4, 6, 11, 7, 9, 3, 5, 12, 0, 18]

k = int(input("Enter k: "))
res = []
win_start = 0
curr_win_sum = 0


for win_end in range(len(arr)):
    curr_win_sum += arr[win_end]

    if win_end >= k - 1:
        res.append(curr_win_sum)
        curr_win_sum -= arr[win_start]
        win_start += 1

print(res)
