"""
Find two numbers in a sorted array that sum to a target.
"""


nums = [1,1,2,3,5,5,6,7,8,9,9,10]
target = int(input("Enter target: "))


def sum_to_target(nums: list[int], target: int) -> tuple[int, int]:
    lp, rp = 0, len(nums) - 1
    
    while (lp < rp):
        sm = nums[lp] + nums[rp]
        if (sm == target):
            return nums[lp], nums[rp]
        elif (sm < target):
            lp += 1
        elif (sm > target):
            rp -= 1
    
    return -1, -1
    

print(sum_to_target(nums, target))