"""
- Find a target sum window (fixed size)
"""

arr = [1, 9, 8, 2, 4, 6, 11, 7, 9, 3, 5, 12, 0, 18]
k = int(input("Enter k: "))
X = int(input("Enter target value: "))

win_start = 0
curr_win_sum = 0


for win_end in range(len(arr)):
    curr_win_sum += arr[win_end]

    if win_end >= k - 1:
        print(arr[win_start : win_end + 1], curr_win_sum)
        if curr_win_sum == X:
            print("Window with target sum starting index:", win_start)
            break

        curr_win_sum -= arr[win_start]
        win_start += 1
