class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [p,q]
        while stack:
            curr_q = stack.pop()
            curr_p = stack.pop()
            if curr_p and curr_q:
                if curr_p.val != curr_q.val:
                    return False
                stack += curr_p.left, curr_q.left
                stack += curr_p.right, curr_q.right
            elif (curr_p!=None and curr_q==None) or (curr_p==None and curr_q!=None):
                return False
        return True
