import cProfile


def harmonic_number_gen(n: int) -> int:
    if n == 1:
        print("[BASE CASE]")
        return 1

    print(f"[COMPUTE] {n} * func({n - 1})")
    return n * harmonic_number_gen(n - 1)


print(harmonic_number_gen(10))

cProfile.run("harmonic_number_gen(700)")
