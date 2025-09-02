import cProfile


def sumPowersOf2_iter(n: int) -> int:
    res = 0
    for i in range(n):
        print(f"res = {res} + 2**{i}")
        res = res + 2**i

    return res


cProfile.run("sumPowersOf2_iter(100)")


def sumPowersOf2_recur(n: int) -> int:
    if n == 0:
        return 1

    print(f"return 2 ** {n} + sumPowersOf2_recur({n - 1})")
    return 2**n + sumPowersOf2_recur(n - 1)


cProfile.run("sumPowersOf2_recur(100)")
