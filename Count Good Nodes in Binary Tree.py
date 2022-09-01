# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def notBigger(root, prev):
            if root is None:
                return 0
            maxx = max(root.val, prev)
            return (root.val>=prev) + notBigger(root.left, maxx) + notBigger(root.right, maxx)
            
        return notBigger(root, root.val)
    
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root, root.val)]
        while stack:
            cur_root, prev_val = stack.pop()
            count += cur_root.val >= prev_val
            for i in cur_root.left, cur_root.right:
                if i:
                    stack.append((i, max(cur_root.val, prev_val)))
        return count
