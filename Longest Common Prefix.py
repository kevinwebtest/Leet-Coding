class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        firstword = strs[0]
        lastword = strs[-1]
        for i in range(len(firstword)):
            if firstword[i] != lastword[i]:
                return firstword[:i]
        return firstword
