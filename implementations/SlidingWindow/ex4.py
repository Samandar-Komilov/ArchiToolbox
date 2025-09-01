"""
    - Find the window with the minimum sum (fixed size)
"""

arr = [1,9,8,2,4,6,11,7,9,3,5,12,0,18]

k = int(input("Enter k: "))
curr_win_sum, min_win_sum = 0, 0
win_start = 0


for win_end in range(len(arr)):
    curr_win_sum += arr[win_end]

    if (win_end >= k - 1):
        if curr_win_sum < min_win_sum or win_start == 0:
            min_win_sum = curr_win_sum
        
        curr_win_sum -= arr[win_start]
        win_start += 1
    

print(min_win_sum)