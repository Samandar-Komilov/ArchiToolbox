"""
    - Average of each window of size K
"""

arr = [1,9,8,2,4,6,11,7,9,3,5,12,0,18]

k = int(input("Enter k: "))
curr_win_sum = 0
avgs = []

win_start = 0


for win_end in range(len(arr)):
    curr_win_sum += arr[win_end]

    if (win_end >= k - 1):
        print("Current Window length:", curr_win_sum)
        avgs.append(curr_win_sum / k)
    
        curr_win_sum -= arr[win_end]
        win_start += 1


print(avgs)