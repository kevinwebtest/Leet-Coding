class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        def orderLevel(root, count, output):
            if root:
                output.append([count,root.val])
                orderLevel(root.left, count+1, output)
                orderLevel(root.right, count+1, output)
        orderLevel(root, 0, output)
        newoutput=[]
        if output:
            length = max(output)[0]
            newoutput= [[] for it in range(length+1)]
            for i, num in output:
                newoutput[i].append(num)
        return newoutput
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        output, level = [], [root]
        while level:
            output.append([node.val for node in level])
            temp = [[node.left,node.right] for node in level]
            level = [notnull for leftright in temp for notnull in leftright if notnull]
        return output
