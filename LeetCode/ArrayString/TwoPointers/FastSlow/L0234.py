"""
PALINDROME LINKED LIST

Given the head of a singly linked list, return true if it is a or false otherwise.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        """Stack based O(n) space solution (WRONG)"""
        stack = []

        while head is not None:
            if not stack or stack[-1] != head:
                stack.append(head)
            else:
                stack.pop(-1)
            head = head.next

        if not stack:
            return True

        return False


# A PURE LINKED LIST question, leave for later
