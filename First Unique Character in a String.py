class Solution:
    def firstUniqChar(self, s: str) -> int:
        counted = {}
        for c in s:
            if c in counted:
                counted[c] += 1
            else:
                counted[c] = 1
        for x in counted:     
            if counted[x] == 1:
                return s.index(x)
        return -1
