"""
Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxnum, num_zeros = 0, 0
        win_start = 0

        for win_end in range(len(nums)):
            if nums[win_end] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[win_start] == 0:
                    num_zeros -= 1

                win_start += 1

            maxnum = max(maxnum, win_end - win_start + 1)

        return maxnum


sl = Solution()
res = sl.longestOnes(
    nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3
)
print(res)
