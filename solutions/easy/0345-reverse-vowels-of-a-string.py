"""
Problem: 345. Reverse Vowels of a String
Category: Strings / Two Pointers

Description: Given a string s, reverse only all the vowels in the string and return it.
             The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases.

Algorithm:

- Set two pointers, one at the start and the other at the end of the string (based on length)
- Create a new list containing the chars of the string
- Iterate over the string using the pointers:
    - If both point to a vowel:
        - swap and slide towards the center both pointers
    - If only one is a vowel:
        - slide the other towards the center
    - If no one points to a vowel:
        - slide both pointers towards the center


Complexity:
- Time: O(n)    # iterate over every element once
- Space: O(n)   # create a list of len(s) (n) elements

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        new_string = list(s)

        i = 0
        j = len(new_string) - 1

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                new_string[i], new_string[j] = new_string[j], new_string[i]
                i+=1
                j -=1
                continue
    
            elif s[i] in vowels:
                j -= 1
                continue
            
            elif s[j] in vowels:
                i += 1
                continue
            else:
                i += 1
                j -= 1

        return ''.join(new_string)