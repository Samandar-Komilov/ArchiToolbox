"""
Check if array is palindrome
"""


class Solution:
    def is_palindrome_array(self, arr: list[int]) -> bool:
        if not arr:
            return True

        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False

            left += 1
            right -= 1

        return True


sl = Solution()
print(sl.is_palindrome_array([1, 2, 3, 2, 1]))
print(sl.is_palindrome_array([]))
print(sl.is_palindrome_array([1, 2, 3, 2]))
print(sl.is_palindrome_array([1, 2, 2, 1]))
