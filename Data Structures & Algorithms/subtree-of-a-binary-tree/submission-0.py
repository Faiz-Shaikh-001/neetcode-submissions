# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            elif not p:
                return False
            elif not q:
                return False
            else:
                left_same = isSame(p.left, q.left)
                right_same = isSame(p.right, q.right)
                curr_same = left_same and right_same and p.val == q.val
                return curr_same
        
        def search(node):
            if not node:
                return False
            
            if isSame(node, subRoot):
                return True
            
            left_subroot = search(node.left)
            right_subroot = search(node.right)

            if left_subroot:
                return True
            return right_subroot
        
        return search(root)

        