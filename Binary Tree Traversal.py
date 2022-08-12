# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Traversal(self, root: Optional[TreeNode]) -> List[int]:
        output1,output2,output3 =[],[],[]
        self.inorder(root, output1)
        self.inorder(root, output2)
        self.inorder(root, output3)
        return output1,output2,output3
        
    def inorder(self, myroot, output):
        if myroot:
            self.inorder(myroot.left, output)
            output.append(myroot.val)
            self.inorder(myroot.right, output)
            
    def preorder(self, myroot, output):
        if myroot:
            output.append(myroot.val)
            self.preorder(myroot.left, output)
            self.preorder(myroot.right, output)
            
    def inorder(self, myroot, output):
        if myroot:
            self.inorder(myroot.left, output)
            self.inorder(myroot.right, output)
            output.append(myroot.val)
    
