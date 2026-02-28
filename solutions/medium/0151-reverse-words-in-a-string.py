"""
Problem: 151. Reverse Words in a String
Category: Strings / Two Pointers (implicit)

Description: Reverse the order of words in a string deleting extra spaces.

Algorithm:

- Get all words by striping and splitting (first remove heading and trailing spaces, then split keeping only non-space characters)
- Create a new string by inserting a space between each word taken in reverse order.

Complexity:
- Time: O(n)    # all methods iterate through the string/list in a linear time
- Space: O(n)   # creating a list based on the length and number of words of the string

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return ' '.join(words[::-1])