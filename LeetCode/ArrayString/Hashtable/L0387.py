"""
FIRST UNIQUE CHARACTER IN A STRING

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

# beats 48.14%, better approach they used ascii chars somehow
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = dict()

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for i in range(0, len(s)):
            if freq[s[i]] == 1:
                return i
        
        return -1