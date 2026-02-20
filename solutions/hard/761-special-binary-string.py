"""
Problem: 761. Special Binary String
Category: Recursion / String Manipulation / Sorting

Description: Find the lexicographically largest special binary string by swapping 
             consecutive special substrings. Special strings have equal 0s and 1s, 
             and every prefix has 1s >= 0s (like balanced parentheses).

Algorithm:

- Iterate over every element of the string
- Count 1's and 0's
- When the amount of 1's and 0's is the same:
    - take the found substring
    - apply the same iteration (recuersion)
- Sort the substrings

Complexity:
- Time: O(n^2)  # sort and slicing on every recursion leve
- Space: O(n)   # creation of substring with size based on the original string

"""

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ''
        count = 0
        subs = []
        start = 0
        for i, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                sub = s[start:i+1]
                subs.append('1' + self.makeLargestSpecial(sub[1:-1]) + '0' )
                start = i + 1
                count = 0
        subs.sort(reverse=True)
        return "".join(subs)