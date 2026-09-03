# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0) #height, diameter
            
            left_height, left_diameter = dfs(root.left)
            right_height, right_diameter = dfs(root.right)

            height = 1 + max(left_height, right_height)
            diameter = left_height + right_height
            max_diameter = max(diameter, left_diameter, right_diameter)
            
            return height, max_diameter
        _, diameter = dfs(root)
        return diameter