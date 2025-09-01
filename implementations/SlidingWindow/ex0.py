"""
    Basic Template for all Sliding Window related questions

    - This implementation computes the sum of each window of the user-specified size and prints to the terminal.
"""

arr = [1,2,3,4,5,6,7,8,4,3,1]

win_start = 0
curr_win_sum = 0

k = int(input("Enter k: "))


for win_end in range(len(arr)):
    curr_win_sum += arr[win_end]

    if (win_end >= k-1):
        print(f"Window [{win_start}:{win_end}] has sum: {curr_win_sum}.")

        curr_win_sum - arr[win_start]
        win_start+=1