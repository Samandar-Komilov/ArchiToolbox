"""
    - Slide a window and collect elements (string focus)
"""

s = "helloworld!"
k = int(input("Enter k: "))

win_start = 0

for win_end in range(len(s)):
    if (win_end >= k - 1):
        print(s[win_start:win_end+1])
    
        win_start+=1

