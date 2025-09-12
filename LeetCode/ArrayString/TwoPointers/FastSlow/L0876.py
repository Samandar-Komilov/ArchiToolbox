"""
MIDDLE OF THE LINKED LIST

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next is not None and fast.next.next is None:
            return slow.next

        return slow
