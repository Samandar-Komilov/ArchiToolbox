"""
    - Minimum/Maximum element in each window of size k (brute-force version)
"""

arr = [1,9,8,2,4,6,11,7,9,3,5,12,0,18]

k = int(input("Enter k: "))
win_start = 0
curr_window, win_mins = [], []

for win_end in range(len(arr)):
    curr_window.append(arr[win_end])

    if (win_end >= k - 1):
        print("Current window:", curr_window)
        win_mins.append(min(curr_window))
        # win_maxs.append(max(curr_window))

        curr_window.pop(0)
        win_start += 1

print(win_mins)

# Non-brute force approach, we used temporary space instead