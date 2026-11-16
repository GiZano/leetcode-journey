"""
Problem: 2114. Maximum Number of Words Found in Sentences
Category: Strings / Arrays

Description: A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
             You are given an array of strings sentences, where each sentences[i] represents a single sentence.
             Return the maximum number of words that appear in a single sentence.

Algorithm:

- for every sentence, split the words and count the number of elements
- return the maximum value found

Complexity:
- Time: O(n * m)  # iteration over all sentences (n) iteration over each sentence (m)
- Space: O(m)     # creation of a temporary sentence with split()

"""

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)