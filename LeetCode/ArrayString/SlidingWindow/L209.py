"""
    Minimum Size Subarray Sum
    - Given an array of positive integers nums and a positive integer target, return the minimal length of a whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class Solution:
    """O(n) solution"""
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        curr_sum, min_len = 0, float('inf')
        win_start = 0

        if (sum(nums) < target):
            return 0

        for win_end in range(len(nums)):
            curr_sum += nums[win_end]
            print("Current sum", curr_sum)

            while (curr_sum >= target):
                min_len = min(min_len, win_end - win_start + 1)
                print("Min len", min_len)

                curr_sum -= nums[win_start]
                win_start += 1
        
        return min_len
    
s = Solution()
res = s.minSubArrayLen(7, [2,3,1,2,4,3])

print(res)

# --------------

class Solution:
    """O(nlog(n)) solution (requires prefix sum and hashtable)"""
    pass