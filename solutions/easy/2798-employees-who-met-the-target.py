"""
Problem: 2798. Number of Employees Who Met the Target
Category: Arrays

Description: There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.
             The company requires each employee to work for at least target hours.

Algorithm:

- Iterate over each time spent by employees
- Add one if time is at least the same as target

Complexity:
- Time: O(n)    # iterating over the whole array once
- Space: O(1)   # no extra variables used

"""

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        return sum(time >= target for time in hours)