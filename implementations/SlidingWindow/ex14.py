"""
    - Minimum size subarray sum (friend of 11)
"""
arr = [2,1,5,2,3,2]

S = int(input("Enter target: "))

curr_win_sum, min_len = 0, float('inf')

win_start = 0


for win_end in range(len(arr)):
    curr_win_sum += arr[win_end]

    while (curr_win_sum >= S):
        min_len = min(min_len, win_end - win_start + 1)

        curr_win_sum -= arr[win_start]
        win_start += 1

print(min_len)