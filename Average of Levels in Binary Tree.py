class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [root]
        average = []
        while stack:
            nodes = len(stack)
            total = 0
            for i in range(nodes):
                curroot = stack.pop(0)
                total += curroot.val
                if curroot.left:
                    stack.append(curroot.left)
                if curroot.right:
                    stack.append(curroot.right)
            average.append(total/nodes)
        return average
