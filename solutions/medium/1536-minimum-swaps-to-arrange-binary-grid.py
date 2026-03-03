"""
Problem: 1536. Minimum Swaps to Arrange a Binary Grid
Category: 2D Arrays / Greedy

Description: Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
             A grid is said to be valid if all the cells above the main diagonal are zeros.
             Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

Algorithm:

- Memorize the position of the latest 1 in each row
- For each row, we need to find a row where the maxRight value is less or equal to i
- If we can't find one, we return -1
- If we find it:
    - We sum the 'swap cost' (j - i)
    - We simulate the swapping with pop and insert

Complexity:
- Time: O(n^2)  # Time to calculate maxRight values and swapping in worst case.
- Space: O(n)   # Creation of maxRight, which is as long as the grid.

"""

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxRight = [-1] * n

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    maxRight[i] = j
        
        swaps = 0

        for i in range(n-1):
            for j in range(i, n):
                if maxRight[j] <= i:
                    swaps += j - i
                    val = maxRight.pop(j)
                    maxRight.insert(i, val)
                    break
            else:
                return -1

        return swaps