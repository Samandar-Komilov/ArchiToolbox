# -------- DEFINITIONS -------- #

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def print_llist(head: Node):
    while head is not None:
        print(head.val, end=", ")
        head = head.next

# -------- SOLUTIONS -------- #
        
def ex11(head: Node) -> bool:
    "Detect cycle in linked list."
    if head is None:
        return False
    
    fast, slow = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if fast == slow:
            # if cycle exists
            return True
    
    return False


def ex12(head: Node) -> Node | None:
    "Find start node of cycle in linked list."
    if head is None:
        return None

    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            break
    
    if fast is None or fast.next is None:
        return None
    
    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    
    return slow
    

def ex13(head: Node) -> Node | None:
    "Find the middle node of linked list."
    if not head:
        return None
    
    fast, slow = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def ex14(head: Node | None, n: int) -> Node | None:
    if not head:
        return None

    if head.next is None:
        head = None
        return head
    
    fast, slow = head, head

    for i in range(n):
        fast = fast.next
    
    while fast and fast.next:
        # first, move fast ptr n times - only for moving slow k times where k = size - n
        slow = slow.next
        fast = fast.next
    
    if not fast:
        # If n is equal to the size of linked list, simply remove head
        head = slow.next
        slow = None
    else:
        # otherwise iterate slow until you find target and delete
        slow.next = slow.next.next

    return head

def ex15(headA: Node, headB: Node) -> Node | None:
    "Find intersection node of two linked lists (if exists)."
    pA, pB = headA, headB

    intersectNode = None
    is_swappedA, is_swappedB = False, False

    while (pA or pB):
        if pA == pB:
            intersectNode = pA
            break
        
        if pA.next is None and not is_swappedA:
            is_swappedA = True
            pA = headB
        else:
            pA = pA.next
        
        if pB.next is None and not is_swappedB:
            is_swappedB = True
            pB = headA
        else:
            pB = pB.next

    return intersectNode


def ex16():
    "Find length of longest palindrome substring using expand-around-center (two pointers growing)."
    pass

        
# -------- TESTS --------- #

def test_ex11():
    # Test case 1: Empty list
    assert ex11(None) == False

    # Test case 2: List with a cycle
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1  # Creating a cycle
    assert ex11(node1) == True

    # Test case 3: List without a cycle
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node4.next = node5
    node5.next = node6
    assert ex11(node4) == False

    print("All test cases passed!")
    
def test_ex13():
    # Test case 1: Empty list
    assert ex13(None) is None

    # Test case 2: List with one node
    node1 = Node(1)
    assert ex13(node1) == node1

    # Test case 3: List with two nodes
    node2 = Node(2)
    node1.next = node2
    assert ex13(node1) == node2

    # Test case 4: List with odd number of nodes
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node3.next = node4
    node4.next = node5
    assert ex13(node3) == node4

    # Test case 5: List with even number of nodes
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node6.next = node7
    node7.next = node8
    assert ex13(node6) == node7

    print("All test cases passed!")
    
def test_ex14():
    print("Leetcode verified (#19).")
    
def test_ex15():
    print("Leetcode verified (#160).")
    

if __name__ == "__main__":
    # test_ex11()
    test_ex13()
    test_ex14()