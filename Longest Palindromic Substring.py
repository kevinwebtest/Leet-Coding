class Solution:
    def longestPalindrome(self, s: str) -> str:
        char = ""
        for i,c in enumerate(s):
            temp = self.findLongest(s, i, i)
            if len(temp)>len(char):
                char = temp
            temp = self.findLongest(s, i, i+1)
            if len(temp)>len(char):
                char = temp
        return char
    
    def findLongest(self, s, l, r):
        while l >= 0 and r < len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
