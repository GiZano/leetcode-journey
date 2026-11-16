"""
Problem: 1404. Number of Steps to Reduce a Number in Binary Representation to One
Category: Bit Manipulation / Math

Description: Given the binary representation of an integer as a string s, return the number 
             of steps to reduce it to 1 under the following rules:
             - If the current number is even, you have to divide it by 2.
             - If the current number is odd, you have to add 1 to it.

Algorithm:

- Transform given binary into integer
- If the number is even:
    - Shift to right by one (elegant and fast / 2)
- If the number is odd:
    - Add one
- Add the steps

Complexity:
- Time: O(n^2)  # creating a new number take O(n), which is done n times (n * n = n^2)
- Space: O(n)   # create an int based on s length

"""

class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        steps = 0
        while num > 1:
            if num % 2 == 0:
                num = num >> 1
            else:
                num += 1
            steps += 1
        
        return steps