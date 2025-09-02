"""
Fibonacci Number
- Given number n, calculate F(n) in the most efficient way.
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)


sl = Solution()
res = sl.fib(4)
print(res)
