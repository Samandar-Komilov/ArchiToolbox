"""
Check if a string is a palindrome ignoring non-alphanumeric chars.
"""

s1 = "abcba"
s2 = "Carre00erraC"
s3 = "rac$eca&r"


def is_palindrome(s: str) -> bool:
    lp, rp = 0, len(s) - 1
    
    while (lp <= rp):
        if not s[lp].isalnum():
            lp += 1
        if not s[rp].isalnum():
            rp -= 1
        if s[lp] != s[rp]:
            return False
        
        lp += 1
        rp -= 1
    
    return True

print(is_palindrome(s1))
print(is_palindrome(s2))
print(is_palindrome(s3))