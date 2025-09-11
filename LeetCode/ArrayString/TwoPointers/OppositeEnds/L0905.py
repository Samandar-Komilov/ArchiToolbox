"""
SORT ARRAY BY PARITY

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1

        return nums


sol = Solution()
print(sol.sortArrayByParity([3, 1, 2, 4]))
print(sol.sortArrayByParity([2, 3, 1, 4, 6, 5, 7]))
