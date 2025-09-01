### 10 Fundamental Practice Questions

**1. Print All Windows of Size K**
**Task:** Given an array and an integer `k`, print every contiguous subarray (window) of size `k`.
**Example:** `arr = [1, 2, 3, 4, 5], k = 3`
**Output:**
`[1, 2, 3]`
`[2, 3, 4]`
`[3, 4, 5]`
**Focus:** This purely practices the mechanics of moving the start and end pointers for a fixed window. No sum, no max, just printing.

**2. Sum of Each Window of Size K**
**Task:** Given an array and an integer `k`, print the sum of each contiguous subarray of size `k`.
**Example:** `arr = [1, 2, 3, 4, 5], k = 3`
**Output:** `6, 9, 12`
**Focus:** Practice managing a running sum. See how you add the new element and subtract the one leaving.

**3. Find the Window with the Maximum Sum (Fixed Size)**
**Task:** Given an array of integers and an integer `k`, find the maximum sum of any contiguous subarray of size `k`.
**Example:** `arr = [2, 1, 5, 1, 3, 2], k = 3` -> Output: `9` (from `[5, 1, 3]`)
**Focus:** This is the classic starter problem. It adds just one step to the previous question: comparing the `current_window_sum` to a `max_sum` variable.

**4. Find the Window with the Minimum Sum (Fixed Size)**
**Task:** Same as #3, but find the *minimum* sum.
**Example:** `arr = [2, 1, 5, 1, 3, 2], k = 3` -> Output: `4` (from `[1, 5, 1]`? Wait, let's calculate: `2+1+5=8`, `1+5+1=7`, `5+1+3=9`, `1+3+2=6`. Actually `1+3+2=6` is the smallest. See, you have to code it to be sure!)
**Focus:** Reinforces the pattern by changing just the comparison logic from `max()` to `min()`.

**5. Average of Each Window of Size K**
**Task:** Given an array and an integer `k`, return an array containing the average of each contiguous subarray of size `k`.
**Example:** `arr = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5`
**Output:** `[2.2, 2.8, 2.4, 3.6, 2.8]`
**Focus:** Same mechanics as summing, but you practice a simple final calculation (`sum / k`). This is a very common real-world application (e.g., moving averages in stock prices).

**6. Maximum Element in Each Window of Size K (Brute-Force Version)**
**Task:** Given an array and an integer `k`, find the maximum element in each window of size `k`. **For now, use a simple inner loop to find the max.**
**Example:** `arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`
**Output:** `[3, 3, 5, 5, 6, 7]`
**Focus:** This is crucial. It makes you separate the **window management** (the sliding) from the **window processing** (finding the max). First, master the sliding. The efficient solution (with a deque) is much harder and comes later.

**7. Count the Number of Windows with Sum > X (Fixed Size)**
**Task:** Given an array of integers, a fixed window size `k`, and a target `X`, count how many windows have a sum greater than `X`.
**Example:** `arr = [1, 2, 3, 4, 5], k=3, X=7` -> Output: `3` (All three windows `[1,2,3]=6`(no), `[2,3,4]=9`(yes), `[3,4,5]=12`(yes) -> wait, that's only 2. Let's recalc: `6<=7`, `9>7`, `12>7`. So output is 2.)
**Focus:** Practices integrating a simple conditional check (`if current_window_sum > X: count += 1`) into the sliding loop.

**8. Slide a Window and Collect Elements (String Focus)**
**Task:** Given a string `s` and an integer `k`, print each contiguous substring of length `k`.
**Example:** `s = "abcdef", k = 3`
**Output:** `"abc", "bcd", "cde", "def"`
**Focus:** Practices applying the identical fixed-window logic to a string data type instead of an array.

**9. Find a Target Sum Window (Fixed Size)**
**Task:** Given an array of integers and a fixed window size `k`, find the **first** window where the sum equals a target value. Return its starting index.
**Example:** `arr = [1, 4, 2, 10, 2, 3, 1, 0], k=4, target=18` -> Output: `3` (The window starting at index 3 is `[10, 2, 3, 1]` which sums to 16. Let's try: Window 0: `1+4+2+10=17`, Window 1: `4+2+10+2=18` -> Found it! Index 1.)
**Focus:** Practices using a `return` or `break` statement inside the window loop once a condition is met.

**10. Basic Variable Window: Find the Length of the Smallest Subarray with Sum >= Target**
**Task:** Given an array of positive integers and a target sum `S`, find the **length** of the smallest contiguous subarray whose sum is **greater than or equal to** `S`.
**Example:** `arr = [2, 1, 5, 2, 3, 2], S=7` -> Output: `2` (The subarray `[5, 2]` has the smallest length that meets the sum.)
**Focus:** This introduces the **variable window** pattern. The window grows until the condition is met (`sum >= S`), and then it shrinks from the left to find the smallest valid window.
```python
window_start = 0
min_length = float('inf')
current_sum = 0

for window_end in range(len(arr)):
    current_sum += arr[window_end] # Add next element

    # This is the key part: Shrink the window as much as possible
    while current_sum >= S:
        min_length = min(min_length, window_end - window_start + 1)
        current_sum -= arr[window_start] # Shrink from the left
        window_start += 1
```

**11. Longest Subarray with Sum <= K (Positive Integers)**
**Task:** Given an array of **positive integers** and a target `k`, find the **length of the longest** contiguous subarray whose sum is **less than or equal to** `k`.
**Why it's good:** This is the simplest variable window. You only shrink the window when the sum becomes *too large* (`> k`). You update the answer when the window is valid (`<= k`).
**Example:** `arr = [3, 1, 2, 7, 1, 1, 1, 1, 5], k = 8`
**Logic:**
- Grow the window (add to `current_sum`).
- When `current_sum > k`, it's invalid. Shrink from the left until `current_sum <= k`.
- The window is now valid. Is its length the longest we've seen? `max_length = max(max_length, window_size)`
**Output:** The longest valid subarray is `[1, 1, 1, 1]` with a sum of 4 and a length of `4`.

**12. Longest Substring Without Repeating Characters (Basic Version - Assume Small Alphabet)**
**Task:** Given a string `s`, find the length of the longest substring without repeating characters. *For practice, you can use a set or a simple list of seen characters.*
**Why it's good:** Introduces the concept of tracking *uniqueness* in a window using a set. You shrink the window until the duplicate is removed.
**Example:** `s = "abccabcbb"`
**Logic:**
- Grow the window, adding characters to a `seen` set.
- If you try to add a duplicate character, the window is invalid.
- Shrink from the left, removing characters from the `seen` set, until the duplicate is gone.
- The window is now valid. Update `max_length`.
**Output:** `3` (e.g., "abc")

**13. Max Consecutive Ones After Flipping K Zeros (Simplified)**
**Task:** Given a binary array (`0`s and `1`s) and an integer `k`, find the maximum number of consecutive `1`s you can achieve by flipping **at most** `k` `0`s to `1`s.
**Why it's good:** Introduces the concept of a "budget" (`k`) for something invalid (`0`s) in the window. You shrink the window only when you exceed your budget.
**Example:** `nums = [1, 1, 0, 0, 1, 1, 1, 0, 1], k = 2`
**Logic:**
- Grow the window.
- Every time you add a `0`, it uses your budget (`zero_count += 1`).
- If `zero_count > k`, the window is invalid. Shrink from the left until `zero_count <= k` (if the left pointer is on a `0`, removing it gives you budget back).
- The window is now valid. Its length is the number of consecutive `1`s you could create. Update `max_length`.
**Output:** `6` (Flip the two zeros in the middle: `[1, 1, 1, 1, 1, 1, ...]`).

**14. Minimum Size Subarray Sum (The counterpart to #1)**
**Task:** Given an array of **positive integers** and a target `S`, find the **length of the smallest** contiguous subarray whose sum is **greater than or equal to** `S`.
**Why it's good:** This is the classic "minimum window" pattern. You update the answer *inside the while loop* at the moment the window becomes valid, as you try to shrink it to find the *smallest* valid window.
**Example:** `arr = [2, 1, 5, 2, 3, 2], S = 7`
**Logic:**
- Grow the window (add to `current_sum`).
- **While** `current_sum >= S` (the window is valid):
    - Update `min_length = min(min_length, window_size)`
    - Shrink from the left (`current_sum -= arr[window_start]`, `window_start += 1`) to try to find a smaller valid window.
**Output:** `2` (The subarray `[5, 2]`).

**15. Longest Substring with At Most K Distinct Characters (The Classic)**
**Task:** Given a string `s` and an integer `k`, find the length of the longest substring that contains **at most** `k` distinct characters.
**Why it's good:** Introduces using a frequency dictionary (or `defaultdict(int)`) to track the contents of the window. You shrink the window based on the size of the dictionary.
**Example:** `s = "araaci", k = 2`
**Logic:**
- Grow the window. For each new char, update its count in `freq_map`.
- **While** `len(freq_map) > k` (the window is invalid):
    - Subtract the count for the char at `window_start`.
    - If its count becomes `0`, `del` it from the `freq_map`.
    - `window_start += 1`
- The window is now valid (`len(freq_map) <= k`). Update `max_length`.
**Output:** `4` (The substring "araa" has distinct chars 'a' and 'r').

---
