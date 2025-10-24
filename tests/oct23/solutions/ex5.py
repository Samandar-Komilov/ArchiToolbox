"""
Merge two sorted arrays into one sorted array (in-place).
"""

# l1 = [1,1,2,3,4,4,5]
# l2 = [2,3,3,4,6,7]

l1 = [0]
l2 = [1]

def merge_arrays(l1: list[int], l2: list[int]) -> list[int]:
    len1, len2 = len(l1), len(l2)
    l1.extend([0]*len2)
    
    wp, rp1, rp2 = len(l1) - 1, len1 - 1, len2 - 1
    while (wp >= 0 and rp1 >= 0 and rp2 >= 0):
        if (rp1 >= 0 and l1[rp1] > l2[rp2]):
            l1[wp] = l1[rp1]
            rp1 -= 1
        else:
            l1[wp] = l2[rp2]
            rp2 -= 1
        
        wp -= 1
    
    return l1

print(merge_arrays(l1, l2))
