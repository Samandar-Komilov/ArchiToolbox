"""
Move all zeros to the end maintaining relative order.
"""

nums = [1, 0, 3, 0, 0, 4, 6, 3, 0, 9]


def move_zeros(nums: list[int]) -> list[int]:
    wp, rp = 0, 0
    
    while (wp < len(nums) and rp < len(nums)):
        if nums[rp] != 0:
            nums[wp], nums[rp] = nums[rp], nums[wp]
            wp += 1
        rp += 1
    
    return None

move_zeros(nums)
print("Result:\n", nums)