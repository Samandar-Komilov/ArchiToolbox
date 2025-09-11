"""
REVERSE STRING

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return None


sol = Solution()
s = ["e", "s", "h", "m", "a", "t"]
sol.reverseString(s)
print(s)
