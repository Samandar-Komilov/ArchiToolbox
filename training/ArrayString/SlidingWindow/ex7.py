"""
- Count the number of windows with sum > X (fixed size)
"""

arr = [1, 9, 8, 2, 4, 6, 11, 7, 9, 3, 5, 12, 0, 18]

k, X = map(int, input().split())

curr_win_sum, cnt = 0, 0
win_start = 0


for win_end in range(len(arr)):
    curr_win_sum += arr[win_end]

    if win_end >= k - 1:
        if curr_win_sum > X:
            print(
                f"Window[{win_start}:{win_end}] sum > {X}",
            )
            cnt += 1

        curr_win_sum -= arr[win_start]
        win_start += 1


print(cnt)
