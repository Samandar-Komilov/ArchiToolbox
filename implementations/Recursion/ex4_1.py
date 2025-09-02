import random


def random_list_gen(n: int) -> list:
    return [random.randint(0, 100) for i in range(n)]


n = 10
randlist = random_list_gen(n)

# ---


def findMaxRecur(lst: list) -> int | None:
    if len(lst) == 0:
        # Validation
        return None

    print("[INFO]", lst)

    if len(lst) == 2:
        # Base Case
        print(f"[OPERATION] {lst[0]} > {lst[1]} = ?")
        return lst[0] if lst[0] > lst[1] else lst[1]

    # Recursive Case
    rest: int = findMaxRecur(lst[1:])

    print(f"[OPERATION] {lst[0]} > {rest} = ?")
    return lst[0] if lst[0] > rest else rest


print(findMaxRecur(randlist))
