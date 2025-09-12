"""
Check if string is a palindrome (ignore case + spaces)
"""


class Solution:
    def is_palindrome_string(self, string: str) -> bool:
        if not string:
            return True
        left, right = 0, len(string) - 1

        while left < right:
            if string[left].isspace():
                left += 1
            elif string[right].isspace():
                right -= 1
            elif string[left].lower() != string[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True


sl = Solution()
print(sl.is_palindrome_string("A man a plan a canal panama"))
print(sl.is_palindrome_string("abba"))
print(sl.is_palindrome_string("hello Guys!@"))
