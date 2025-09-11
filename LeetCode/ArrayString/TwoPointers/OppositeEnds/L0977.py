"""
SQUARES OF SORTED ARRAY

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """O(n) solution"""
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        resp = right

        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                res[resp] = (nums[right]) ** 2
                resp -= 1
                right -= 1
            else:
                res[resp] = (nums[left]) ** 2
                resp -= 1
                left += 1

        return res

    def old(self, nums: list[int]) -> list[int]:
        """O(nlogn) solution"""
        return sorted([x**2 for x in nums])


sol = Solution()
print(sol.sortedSquares([-4, -1, 0, 3, 10]))
print(sol.sortedSquares([-7, -3, 2, 3, 11]))
