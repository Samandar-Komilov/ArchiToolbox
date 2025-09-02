"""
Longest Subarray of 1's After Deleting One Element
- Given a binary array nums, you should delete one element from it.
- Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        num_zeros, max_len = 0, 0
        win_start = 0

        for win_end in range(len(nums)):
            if nums[win_end] == 0:
                num_zeros += 1

            while num_zeros > 1:
                if nums[win_start] == 0:
                    num_zeros -= 1

                win_start += 1

            max_len = max(max_len, win_end - win_start - num_zeros + 1)

        return max_len if max_len != len(nums) else max_len - 1


sl = Solution()
res = sl.longestSubarray([1, 1, 1])
print(res)
