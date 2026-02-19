"""
Problem: 1786. Merge Strings Alternately
Category: Two Pointers

Description: Given two strings (word1, word2), merge them alternatively until one ends, and add the rest of the other string at the end.

Algorithm:

- Find the minimum length between the words
- Merge the words alternatively until one ends (based on min_len)
- Add the rest of the other string (by adding bot [min_len:], as if the index in string slicing is out of bounds, it will just return an empty string)

Complexity:
- Time:  O(n + m)   # picking every char to concatenate it to the final string
- Space: O(n + m)   # creating a new string using the two given

"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        result = ""
        for i in range(min_len):
            result += word1[i] + word2[i]
        
        result += word1[min_len:] + word2[min_len:]

        return result