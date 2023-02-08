class Solution:
    def isValidBST(self, root: Optional[TreeNode], upper=float('inf'), lower=float('-inf')) -> bool:
        if not root:
            return True
        if root.val<=lower or root.val>=upper:
            return False
        return self.isValidBST(root.left, root.val, lower) and self.isValidBST(root.right, upper, root.val)