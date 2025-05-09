import cProfile

def str_to_int(s: str) -> int:
    ln = len(s)
    if ln == 1:
        print("Base Case")
        return int(s)

    print("Recursive case")
    return int(s[0]) * 10 ** (ln - 1) + str_to_int(s[1:])

print(str_to_int("12356"))

# Trash implementation :))