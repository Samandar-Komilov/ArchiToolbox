"""
Remove Duplicates: Remove duplicates from sorted array in-place, return new length
"""

class Solution:
    def remove_duplicates(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1

        while (left < right):
            pass