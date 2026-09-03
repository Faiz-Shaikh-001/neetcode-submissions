# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root, level, maxx):
            if not root:
                maxx = max(maxx, level)
                level -= 1
                return maxx
            
            level += 1
            max_left = dfs(root.left, level, maxx)
            max_right = dfs(root.right, level, maxx)

            return max(max_left, max_right)
        return dfs(root, 0, 1)