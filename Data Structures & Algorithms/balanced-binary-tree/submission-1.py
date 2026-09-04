# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0, True

            left_height, left_balanced = height(root.left)
            right_height, right_balanced = height(root.right)

            is_node_balanced = abs(left_height - right_height) <= 1
            current_balanced = left_balanced and right_balanced and is_node_balanced

            current_height = 1 + max(left_height, right_height)
            return current_height, current_balanced
        
        return height(root)[1]


