"""
    - Longest Substring Without Repeating Characters (assume small alphabet)
"""

s = "abccabcbb"
max_len = 0
seen = set()

win_start = 0


# for win_end in range(len(s)):