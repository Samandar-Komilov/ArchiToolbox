def ex1(l: list[int], target: int) -> tuple[int, int]:
    """Two numbers sum to target"""
    lp, rp = 0, len(l) - 1
    
    while lp < rp:
        if l[lp] + l[rp] == target:
            return l[lp], l[rp]
        lp += 1
        rp -= 1
    
    return -1, -1


def ex2(s: str) -> bool:
    """String is palindrome?"""
    lp, rp = 0, len(s) - 1
    
    while lp < rp:
        if s[lp] != s[rp]:
            return False
        lp += 1
        rp -= 1
    
    return True


def ex3(l1: list[int], l2: list[int]) -> list[int]:
    "Merge two sorted arrays"
    l1_len, l2_len = len(l1), len(l2)
    l1.extend([0]*l2_len)
    
    wp, rp1, rp2 = len(l1)-1, l1_len - 1, l2_len - 1
    
    if (rp1 < 0 and rp2 < 0):
        return []
    
    while (wp >= 0):
        if (rp1 < 0):
            l1[wp] = l2[rp2]
            rp2 -= 1
        elif (rp2 < 0):
            l1[wp] = l1[rp1]
            rp1 -= 1
        else:
            if (rp1 >= 0 and l1[rp1] >= l2[rp2]):
                l1[wp] = l1[rp1]
                rp1 -= 1
            else:
                l1[wp] = l2[rp2]
                rp2 -= 1
        wp -= 1
    
    return l1


def ex3_2(l1: list[int], l2: list[int]) -> list[int]:
    "Merge two sorted arrays"
    l1_len, l2_len = len(l1), len(l2)
    l1.extend([0]*l2_len)
    
    wp, rp1, rp2 = len(l1)-1, l1_len - 1, l2_len - 1
    
    while (rp2 >= 0):
        if (rp1 >= 0 and l1[rp1] > l2[rp2]):
            l1[wp] = l1[rp1]
            rp1 -= 1
        else:
            l1[wp] = l2[rp2]
            rp2 -= 1
        wp -= 1
        
    return l1


def ex4(l: list[int]) -> tuple[list[int], int]:
    "Remove all duplicates from a sorted array (return length)."
    if not l:
        return [], 0
    
    wp, rp = 0, 1
    
    while (rp < len(l)):
        if (l[wp] == l[rp]):
            rp += 1
        else:
            wp += 1
            l[wp] = l[rp]
            rp += 1
    
    return l[:wp+1], wp+1


def ex5(l: list[int], val: int) -> list[int]:
    "Remove a given value in place from array."
    wp, rp = 0, 0
    
    while (rp < len(l)):
        if l[rp] != val:
            l[wp] = l[rp]
            wp += 1
        rp += 1
    
    del l[wp:]
    return l

def ex6(nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        resp = right

        while (left <= right):
            if (abs(nums[left]) <= abs(nums[right])):
                res[resp] = (nums[right])**2
                resp -= 1
                right -= 1
            else:
                res[resp] = (nums[left])**2
                resp -= 1
                left += 1
            
        return res

def ex7(l: list[int]) -> list[int]:
    "Move all zeros to the end while maintaining order."
    wp, rp = 0, 0
    
    while (rp < len(l)):
        if (l[rp] != 0):
            l[wp] = l[rp]
            wp += 1
        rp += 1
    
    while (wp < len(l)):
        l[wp] = 0
        wp += 1
    
    return l

def ex8(s: str) -> str:
    "Reverse words in a string in place (no split/extra array)."
    words = s.strip().split()

    lp, rp = 0, len(words) - 1
    while (lp < rp):
        words[lp], words[rp] = words[rp], words[lp]
        lp += 1
        rp -= 1
    
    return " ".join(words)

def ex9(l: list[int]) -> list[int]:
    "Partition array into negatives and non-negatives in place."
    lp, rp = 0, len(l) - 1
    
    while (lp < rp):
        if l[lp] < 0:
            lp += 1
        if l[rp] > 0:
            rp -= 1
        elif l[lp] > 0 and l[rp] < 0:
            l[lp], l[rp] = l[rp], l[lp]
            lp += 1
            rp -= 1
        
    return l

def ex10(lines: list[int]) -> tuple[int, int, int]:
    "Find the container with most water (max area between two lines)."
    lp, rp = 0, len(lines) - 1
    maxvol = 0
    
    while lp < rp:
        maxvol = max(maxvol, (rp - lp)*min(lines[lp], lines[rp]))
    
        if lines[lp] < lines[rp]:
            lp += 1
        else:
            rp -= 1
    
    return maxvol, lp, rp
    
    

# ============= TESTS ==============

def test_ex1():
    lst = [1,2,5,1,3,5,8,10,9]
    print(ex1(lst, 6))

def test_ex2():
    print(ex2("racecar"))

def test_ex3():
    print(ex3([1,3,5,8,9,10], [2,3,4,6,7]))
    print(ex3([], []))
    print(ex3([], [5]))
    print(ex3([2], [5]))
    print(ex3([], [1,2,3,4]))
    print(ex3_2([1,3,5,8,9,10], [2,3,4,6,7]))
    print(ex3_2([], []))
    print(ex3_2([], [5]))
    print(ex3_2([2], [5]))
    print(ex3_2([], [1,2,3,4]))
    
def test_ex4():
    print(ex4([1,2,2,3,4,4,5,6,7,7]))
    print(ex4([]))
    print(ex4([1]))
    print(ex4([1,1]))
    print(ex4([1,1,2]))
    
def test_ex5():
    print(ex5([], 5))
    print(ex5([5], 10))
    print(ex5([5], 5))
    print(ex5([5,4,3,2,1], 10))
    print(ex5([5,3,2,1], 2))
    print(ex5([3,4,4,5,1], 4))
    
def test_ex6():
    print(ex6([1,2,3,3,5,6]))
    print(ex6([-4,-1,0,3,10]))
    
def test_ex7():
    print(ex7([1,0,7,8,0,0,2,3,4,5]))
    print(ex7([]))
    print(ex7([0,0,0,0]))
    print(ex7([1,2,3,4]))
    print(ex7([0,1,0,2,2,4]))
    print(ex7([1,2,3,0,0]))
    
def test_ex8():
    print(ex8("  hello world   "))
    
def test_ex9():
    print(ex9([1,-2,3,4,-6,-7, -9, -3]))
    print(ex9([]))
    print(ex9([-1,1]))
    print(ex9([0]))
    print(ex9([1]))
    
def test_ex10():
    print(ex10([1,8,6,2,5,4,8,3,7]))

# ============ RUN =============

if __name__ == "__main__":
    # test_ex1()
    # test_ex2()
    # test_ex3()
    # test_ex4()
    # test_ex5()
    # test_ex6()
    # test_ex7()
    # test_ex8()
    # test_ex9()
    test_ex10()