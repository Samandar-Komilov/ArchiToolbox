# Array problems - Discussion

### L0011 - Container With Most Water 🟡

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ln = len(height)
        start, end = 0, ln-1
        maxvol = min(height[start], height[end]) * (end - start)

        while (start < end):
            maxvol = max(maxvol, min(height[end], height[start]) * (end-start))

            if (height[start] < height[end]):
                start+=1
            else:
                end-=1
        
        return maxvol
```

### L0035 - Search Insert Position 🟢

We should discuss why to return start pointer instead of mid if no target is found.

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while (start <= end):
            mid = (start + end) // 2

            if (nums[mid] == target):
                return mid

            if (nums[mid] < target):
                start = mid + 1
            if (nums[mid] > target):
                end = mid - 1
        
        return start
```

### L0066 - Plus One 🟢


```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        end = len(digits) -1
        carry = 0

        digits[end] += 1
        if (digits[end] <= 9):
            return digits
        
        while end >= 0:
            res = digits[end] + carry
            digits[end] = res % 10
            carry = res // 10

            print(res, carry)

            if carry == 0:
                break
            
            if end == 0 and carry != 0:
                digits = [carry] + digits
                break

            end -= 1

        return digits
```