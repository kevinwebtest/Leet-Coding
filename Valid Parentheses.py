class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if ((i=="(") or (i=="[") or (i=="{")):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                lastappendstack = stack.pop()
                if (((i == ")") & (lastappendstack !="(")) \
                    | ((i == "]") & (lastappendstack !="[")) \
                    | ((i == "}") & (lastappendstack !="{"))):
                    return False
        return len(stack) == 0
