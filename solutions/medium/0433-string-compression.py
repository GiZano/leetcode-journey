"""
Problem: 443. String Compression
Category: Strings / Arrays / Two Pointers

Description: Given an array of characters chars, compress it using the following algorithm:
             Begin with an empty string s. For each group of consecutive repeating characters in chars:
             - If the group's length is 1, append the character to s.
             - Otherwise, append the character followed by the group's length.
             The compressed string s should not be returned separately, but instead, be stored in the 
             input character array chars. Note that group lengths that are 10 or longer will be split 
             into multiple characters in chars.
             Return the new length of the array. You must write an algorithm that uses only O(1) extra space.

Algorithm:

- Initialize read and write pointers
- While the read pointer hasn't reached the end:
    - Count all the identical characters
    - Only modify the part of the string where the write variable is pointing
- Return the length

Complexity:
- Time: O(n)    # Iterate over the string once
- Space: O(1)   # Only use pointers

"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                count += 1
                read += 1
            
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write