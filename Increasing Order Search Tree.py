# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        def inorder(node):
            if node:
                inorder(node.left)
                stack.append(node.val)
                inorder(node.right)
        inorder(root)
        newTree = TreeNode(stack[0])
        head = newTree
        for i in stack[1:]:
            head.right = TreeNode(i)
            head = head.right
        return newTree
            