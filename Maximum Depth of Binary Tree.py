# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count=0
        return self.countDepth(root, count)
    
    def countDepth(self, root, count):
        if not root:
            return count
        return max(self.countDepth(root.left, count+1), self.countDepth(root.right, count+1))
