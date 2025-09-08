"""
Remove Duplicates from Sorted Array (in-place)
"""

def remove_duplicates(arr: list[int]):
    if not arr:
        return []
    
    wp, rp = 0, 1

    while (wp < len(arr) and rp < len(arr)):
        if (arr[rp] == arr[wp]):
            rp += 1
        else:
            wp += 1
            arr[wp] = arr[rp]
        
    return arr[:wp+1]

print(remove_duplicates([1,2,2,3,3,4]))