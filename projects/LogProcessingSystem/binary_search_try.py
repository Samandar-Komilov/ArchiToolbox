lst = [1,2,4,5,7,9,11,14,17,19]

def binary_search(lst, x):
    start, end = 0, len(lst) - 1
    closest_bigger = None
    
    while start <= end:
        mid = (start + end) // 2
        
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            closest_bigger = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return closest_bigger if closest_bigger is not None else -1

print(binary_search(lst, 15))
print(binary_search(lst, 19))
print(binary_search(lst, 20))