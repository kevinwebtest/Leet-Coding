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
            length,_ = max(output)
            newoutput= [[] for it in range(length+1)]
            for i, num in output:
                newoutput[i].append(num)
        return newoutput
