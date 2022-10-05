class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if ((i=="(") or (i=="[") or (i=="{")):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
