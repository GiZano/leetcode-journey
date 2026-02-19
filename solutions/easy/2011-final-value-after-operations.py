"""
Problem: 2011. Final Value of Variable After Performing Operations
Category: Arrays / Strings

Description: [Explain the problem]

Algorithm:

- [Point 1]
- [Point 2]
...
- [Point n]

Complexity:
- Time: O(...)
- Space: O(...)

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