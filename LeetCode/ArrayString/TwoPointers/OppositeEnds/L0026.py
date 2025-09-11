"""
REMOVE DUPLICATES FROM SORTED ARRAY
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """O(n) solution, write-read pointers"""
        if not nums:
            return []

        wp, rp = 0, 1

        while wp < len(nums) and rp < len(nums):
            if nums[rp] == nums[wp]:
                rp += 1
            else:
                wp += 1
                nums[wp] = nums[rp]

        return nums[: wp + 1]
