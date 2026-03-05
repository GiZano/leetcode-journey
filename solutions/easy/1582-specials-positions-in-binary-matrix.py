"""
Problem: 1582. Special Positions in a Binary Matrix
Category: 2D Arrays

Description: Given an m x n binary matrix mat, return the number of special positions in mat.
             A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 
             (rows and columns are 0-indexed).

Algorithm:

- Count how many ones are present in each row and column
- Cross check each position without having to check again the whole grid for each position
- Count each special position and return the count

Complexity:
- Time: O(N*M)    # Reading the N*M matrix twice
- Space: O(N+M)   # Creating two lists to store the sum of each row and column

"""

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [0] * n
        cols = [0] * m
        count = 0

        for i in range(n):
            for j in range(m):
                rows[i] += mat[i][j]
                cols[j] += mat[i][j]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    count += 1
        return count