"""
TWO SUM II - INPUT ARRAY IS SORTED

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Two Pointers Solution O(n)"""
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

    def twoSumBinSearch(self, numbers: list[int], target: int) -> list[int]:
        """Binary Search Solution O(nlog(n))"""
        for i in range(0, len(numbers - 1)):
            idx2 = self.binary_search(numbers, target - numbers[i])
            if idx2 >= 0:
                return [i, idx2]

        return []

    def binary_search(self, numbers: list[int], key: int) -> int:
        pass


sol = Solution()
print(sol.twoSum([2, 7, 9, 15], 11))
