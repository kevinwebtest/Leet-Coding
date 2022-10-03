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
        self.preorder(root, output2)
        self.postorder(root, output3)
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
            
    def postorder(self, myroot, output3):
        if myroot:
            self.postorder(myroot.left, output3)
            self.postorder(myroot.right, output3)
            output3.append(myroot.val)
    
class Solution:
    def preorderTraversal(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = [[root, False]]
        while stack:
            nowroot, visited = stack.pop()
            if nowroot:
                if visited:
                    output.append(nowroot.val)
                else:
                    stack.append([nowroot, True])
                    stack.append([nowroot.right, False])
                    stack.append([nowroot.left, False])
        return output

