"""
Problem: 3856. Trim Trailing Vowels
Category: Strings / Two Pointers

Description: Given a whole lowercase english string, return it without the trailing vowels.

Algorithm:

- Use a set for comparation (hash -> O(1))
- Check positions from the end to the front
    - If we find a vowel
        - decrement the 'end' pointer, used later to slice the string
    - Else we exit the loop
- Return the sliced string if any vowels has been found, else return the same string

Complexity:
- Time: O(N)    # in worst case we check every position
- Space: O(1)   # define only integer variables and a fixed length set

"""

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = set('aeiou')
        end = -1
        length = len(s)

        for i in range(length):
            if s[-1 - i] in vowels:
                end -= 1
            else:
                break
        if end == -1:
            return s
        else:
            return s[:end+1]
        
        # fast solution:
        '''
        class Solution:
            def trimTrailingVowels(self, s: str) -> str:
                return s.rstrip('aeiou')
        '''