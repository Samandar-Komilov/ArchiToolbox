"""
MOVE ZEROES
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        1) Left-right pointers, no order
        """
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] != 0:
                left += 1
            elif nums[right] == 0:
                right -= 1

        return None

    def moveZeroes2(self, nums: list[int]) -> None:
        """Read-Write pointers, order preserved"""
        wp, rp = 0, 0

        while wp < len(nums) and rp < len(nums):
            if nums[rp] != 0:
                nums[wp], nums[rp] = nums[rp], nums[wp]
                wp += 1

            rp += 1

        return None


sol = Solution()
n = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
sol.moveZeroes2(n)
print(n)
