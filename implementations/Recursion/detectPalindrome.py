import cProfile

def detect_palindrome(s: str) -> bool:
    if len(s) == 0 or len(s) == 1:
        return True
    
    print(f"s={s}")
    return s[0] == s[-1] and detect_palindrome(s[1:-1])

print(detect_palindrome("baracecarab"))

cProfile.run('detect_palindrome("thisissisiht")')