"""
    Maximum Average Subarray I
    
    - integer array nums[n]
    - integer k
    
    - Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_win_sum, max_avg = 0, 0.0
        win_start = 0

        for win_end in range(len(nums)):
            curr_win_sum += nums[win_end]

            if (win_end >= k - 1):
                max_avg = float(max(max_avg, curr_win_sum / k))

                curr_win_sum -= nums[win_start]
                win_start += 1
        
        return max_avg
    

s = Solution()
res = s.findMaxAverage([1,12,-5,-6,50,3], 4)
print(res)


"""
    A more optimized solution can be like this.
    - This solution stores the first k element's sum as current and max sum, then starts iterating from kth index.
    - This gives it not to use minus infinity
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]

            max_sum = max(max_sum, curr_sum)

        return max_sum / k
    