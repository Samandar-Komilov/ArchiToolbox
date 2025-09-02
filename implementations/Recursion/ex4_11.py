"""
Describe an efﬁcient recursive function for solving the element unique-
ness problem, which runs in time that is at most O(n2 ) in the worst case
without using sorting.
"""

randlist = [1, 2, 3, 4, 5, 6, 6]

# ---


def is_unique_elements(lst: list) -> bool:
    if len(lst) == 1:
        return True

    if not is_unique_element_x(lst[0], lst[1:]):
        return False

    return True and is_unique_elements(lst[1:])


def is_unique_element_x(x: int, lst: list) -> bool:
    if len(lst) == 0:
        return True

    if len(lst) == 1:
        print(f"[BASECASE] {x} != {lst[0]} = ?")
        return x != lst[0]

    print(f"[OPERATION] {x} != {lst[0]} = ?")
    return (x != lst[0]) and is_unique_element_x(x, lst[1:])


print(is_unique_elements(randlist))
