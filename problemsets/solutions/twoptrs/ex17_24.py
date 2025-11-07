# ========= SOLUTIONS ========== #

def ex17(nums: list[int], k: int) -> int:
    "Find max sum of subarray of length *k*."
    if k > len(nums):
        return sum(nums)
    
    lp, rp = 0, k
    maxsum = float("-inf")
    
    while (rp <= len(nums)):
        maxsum = max(maxsum, sum(nums[lp:rp]))
        lp += 1
        rp += 1
    
    return maxsum


def ex17_1(nums: list[int], k: int) -> int:
    lp, rp = 0, k
    maxsum = 0

    while (rp <= len(nums)):
        hs = set()
        is_valid = True

        for i in range(lp, rp):
            if nums[i] in hs:
                is_valid=False
                break
            hs.add(nums[i])

        if is_valid:
            maxsum = max(maxsum, sum(nums[lp:rp]))
            print("Valid!", maxsum, hs, nums[lp:rp])
            rp += 1
            lp += 1
            print(hs, rp, lp)
        else:
            rp += 1
            lp += 1
            print(hs, rp, lp)
            continue
    
    return maxsum


def ex17_2(nums: list[int], m: int, k: int) -> int:
    lp = 0
    maxsum, currsum = 0, 0
    window_freq = dict()

    for rp in range(len(nums)):
        window_freq[nums[rp]] = window_freq.get(nums[rp], 0) + 1
        currsum += nums[rp]

        while rp - lp + 1 > k:
            window_freq[nums[lp]] -= 1
            if window_freq[nums[lp]] == 0:
                del window_freq[nums[lp]]
            currsum -= nums[lp]
            lp += 1
        
        if rp - lp + 1 == k and len(window_freq) >= m:
            maxsum = max(maxsum, currsum)
    
    return maxsum


def ex18(nums: list[int], target: int) -> int:
    "Find smallest subarray with sum ≥ target."
    lp, rp = 0, 0
    currsum = 0
    minlen = float("inf")
    
    if sum(nums) < target:
        return 0
    
    for rp in range(len(nums)):
        currsum += nums[rp]
        
        while (currsum >= target):
            minlen = min(minlen, rp - lp + 1)
            currsum -= nums[lp]
            lp += 1
    
    return minlen


# def ex19()
    

# ========= TESTS ========== #

def test_ex17():
    assert ex17([1,2,3,4,5], 6) == 15
    assert ex17([1,2,3,4,5,6], 4) == 18
    assert ex17([-1,-2,-3,-4,-5], 2) == -3
    assert ex17([0,0,0,0,0], 2) == 0
    print("All test cases passed!")
    
def test_ex17_1():
    print("Passed LeetCode tests!")
    
def test_ex17_2():
    print("Passed LeetCode tests!")
    
def test_ex18():
    assert ex18([1], 2) == 0
    assert ex18([1,2,3,4,5], 10) == 3
    assert ex18([1,2,3,4,5], 12) == 3
    assert ex18([1,2,3,4,5], 1) == 1
    assert ex18([1,2,3,4,5], 5) == 1
    assert ex18([1,2,3,4,5], 15) == 5
    assert ex18([1,2,3,4,5], 20) == 0
    print("All test cases passed!")

# ========= EXECUTION ========== #

if __name__ == "__main__":
    # test_ex17()
    test_ex18()