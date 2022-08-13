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
        
    def inorder(self, myroot, output1):
        if myroot:
            self.inorder(myroot.left, output1)
            output1.append(myroot.val)
            self.inorder(myroot.right, output1)
            
    def preorder(self, myroot, output2):
        if myroot:
            output2.append(myroot.val)
            self.preorder(myroot.left, output2)
            self.preorder(myroot.right, output2)
            
    def inorder(self, myroot, output3):
        if myroot:
            self.inorder(myroot.left, output3)
            self.inorder(myroot.right, output3)
            output3.append(myroot.val)
    
