"""
Problem: 1456. Maximum Number of Vowels in a Substring of Given Length
Category: Arrays / Sliding Window

Description: Given a string and a length for substrings, find the maximum number of vowels
             inside a substring.

Algorithm:

- Define a set with vowels (set -> direct access, list -> needs iteration)
- Calculate the vowel count in the first window
- Slide through the item starting from the one after the first window:
    - If we found a new vowel, increment the total
    - If we just left a vowel, decrement the total
    - Save the maximum between the current and the saved one

Complexity:
- Time: O(n)  # Iterate over the string once 
- Space: O(1) # Only use integers and a fixed len list (for vowels)

"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        total = 0
        for char in s[:k]:
            if char in vowels:
                total += 1

        max_total = total

        for i in range(k, len(s)):
            if s[i] in vowels:
                total += 1
            if s[i - k] in vowels:
                total -= 1
            max_total = max(max_total, total)
        
        return max_total