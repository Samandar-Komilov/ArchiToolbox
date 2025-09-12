"""
- Print all windows of size k
"""

arr = [1, 9, 8, 2, 4, 6, 11, 7, 9, 3, 5, 12, 0, 18]

k = int(input("Enter k: "))

win_start = 0

for win_end in range(len(arr)):
    if win_end >= k - 1:
        print(arr[win_start : win_end + 1])
        win_start += 1
