# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # If both are null 
            if not p and not q:
                return True

            elif not p:
                return False
            elif not q:
                return False
            else:
                left_same = dfs(p.left, q.left)
                right_same = dfs(p.right, q.right)
                curr_same = left_same and right_same and p.val == q.val
                return curr_same
        
        return dfs(p, q)