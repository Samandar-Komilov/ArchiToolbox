import cProfile

def fibo_iter(n: int) -> int:
    a, b = 1, 1
    for _ in range(1, n+1):
        a, b = b, a + b
        print(f"a: {a}, b: {b}")
    return a

def fibo_recur(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fibo_recur(n-1) + fibo_recur(n-2)


# cProfile.run('fibo_iter(1000)')
cProfile.run('fibo_recur(40)')