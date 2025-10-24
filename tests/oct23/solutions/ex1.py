"""
Remove duplicates from sorted array in-place.
"""

l = [1, 1, 2, 2, 3, 3, 4, 4, 5]


def remove_dups(l: list[int]) -> list[int]:
    wp, rp = 0, 1
    
    while (wp < len(l) and rp < len(l)):
        if (l[wp] == l[rp]):
            rp+=1
        else:
            wp+=1
            l[wp] = l[rp]
            rp += 1
    
    return l[0:wp+1]


print(remove_dups(l))