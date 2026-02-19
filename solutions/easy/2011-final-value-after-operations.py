"""
Problem: 2011. Final Value of Variable After Performing Operations
Category: Arrays / Strings

Description: Starting from 0, add 1 whenever there is X++ or ++X in the list, remove 1 whenever there is X-- or --X

Algorithm:

- Iterate over every item in the list
    - Check only the second char, as it always contains the operation symbol
    - Add or remove 1 accordingly


Complexity:
- Time: O(n)    # iteration over the whole list
- Space: O(1)   # using only one variable

"""

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for operation in operations:
            if operation[1] == '+':
                x += 1
            else:
                x -= 1
        return x