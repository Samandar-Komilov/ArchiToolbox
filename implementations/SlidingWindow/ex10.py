"""
    - Find the length if smallest subarray with sum >= target
"""

arr = [2, 1, 5, 2, 3, 2]
X = int(input("Enter target: "))

win_start = 0
min_len = float('inf')
curr_sum = 0


for win_end in range(len(arr)):
    curr_sum += arr[win_end]
    print(f"Current sum of arr[{win_start}:{win_end+1}] = {curr_sum}")
    while (curr_sum >= X):
        min_len = min(min_len, win_end - win_start + 1)
        print("Min length:", min_len)
        curr_sum -= arr[win_start]
        win_start += 1

print(min_len)