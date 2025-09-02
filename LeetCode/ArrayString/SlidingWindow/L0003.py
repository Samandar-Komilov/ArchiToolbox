"""
Longest Substring Without Repeating Characters
- Given a string s, find the length of the longest substring without duplicate characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        chars = set()
        win_start = 0

        for win_end in range(len(s)):
            while s[win_end] in chars:
                chars.remove(s[win_start])
                win_start += 1

            chars.add(s[win_end])
            maxlen = max(maxlen, win_end - win_start + 1)

        return maxlen


sl = Solution()
res = sl.lengthOfLongestSubstring("bbbbbb")
print(res)

"""
    # We used the varying-size sliding window technique, where we encounter a string with duplicate characters, we remove chars from start until the string again becomes correct, while tracking the biggest substring which satisfies the requirement.
"""
