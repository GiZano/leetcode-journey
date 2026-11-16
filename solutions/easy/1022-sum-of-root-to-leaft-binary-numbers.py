"""
Problem: 1022. Sum of Root To Leaf Binary Numbers
Category: Trees / Depth-First Search (DFS)

Description: You are given the root of a binary tree where each node has a value 0 or 1. 
             Each root-to-leaf path represents a binary number starting with the most significant bit.
             Return the sum of these numbers.

Algorithm:

- Create starting variables (final list for all found endpoints, father_path string to remember the walked path)
- Walk through the whole tree:
    - If node isn't defined:
        - return to not cause errors
    - Add current value to the walked path
    - If there aren't branches next:
        - Add the current value (in int) to the final list
    - Else walk through the next branches (right and left)

Complexity:
- Time: O(n)  # we visit every node once
- Space: O(h) # tree height - call stack depth and string size -> worst O(n), balanced O(log n)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pre_order_dfs(self, node, father_path, final):
        if node is None:
            return
        father_path += str(node.val)
        if node.left is None and node.right is None:
            final.append(int(father_path, 2))
        else:
            self.pre_order_dfs(node.left, father_path, final)
            self.pre_order_dfs(node.right, father_path, final)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        final = []
        father_path = ''
        self.pre_order_dfs(root, father_path, final)
        return sum(final)