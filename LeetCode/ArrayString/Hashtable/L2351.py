"""
FIRST LETTER TO APPEAR TWICE

Given a string s consisting of lowercase English letters, return the first letter to appear twice.
"""

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        st = set()

        for c in s:
            if c in st:
                return c
            st.add(c)