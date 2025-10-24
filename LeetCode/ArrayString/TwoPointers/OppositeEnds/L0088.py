"""
MERGE SORTED ARRAY

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(0, n):
            nums1[m + i] = nums2[i]

        nums1.sort()
    
    def merge_better(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        wp, rp1, rp2 = len(nums1) - 1, m - 1, n - 1
        
        while (rp2 >= 0):
            if (rp1 >= 0 and nums1[rp1] > nums2[rp2]):
                nums1[wp] = nums1[rp1]
                rp1 -= 1
            else:
                nums1[wp] = nums2[rp2]
                rp2 -= 1
            
            wp -= 1


sol = Solution()
n1, n2 = [1, 2, 3, 0, 0, 0], [6, 7, 8]
sol.merge_better(n1, 3, n2, 3)
print(n1)
