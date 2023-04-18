class Solution:
    def countSubstrings(self, s: str) -> int:
        def substring(i, j, count):
            while (i>=0 and j<len(s) and s[i]==s[j]):
                i-=1
                j+=1
                count+=1

            return count
        count = 0
        for i in range(len(s)):
            count += substring(i, i, 0)
            count += substring(i, i+1, 0)
        return count