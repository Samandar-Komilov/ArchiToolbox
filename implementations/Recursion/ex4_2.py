import cProfile

def power(x: int, n: int) -> int:
    if n == 0:
        print(f"[OPERATION] {x}**{n}")
        return 1

    print(f"[OPERATION] {x}**{n}")
    partial = power(x, n // 2)
    res = partial * partial

    if n % 2 == 1:
        res *= x
    print(f"[RETURNING] res={res}")
    return res


print(power(2,6))