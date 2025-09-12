def reverse_str(s: str) -> str:
    if len(s) == 0 or len(s) == 1:
        return s

    print(f"s[0]={s[0]} | s={s}")
    return reverse_str(s[1:]) + s[0]


print(reverse_str("This is a racecar!"))


def reverse_str_iter(s: str) -> str:
    res = ""
    while len(s) >= 1:
        print(f"s[0]={s[0]} | s={s}")
        res = s[0] + res
        s = s[1:]

    return res


print(reverse_str("This is!"))
