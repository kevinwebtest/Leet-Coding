class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for ch in s:
            if ch.isalnum():
                new += ch
        for i in range(len(new)//2):
            if new[i] != new[-1-i]:
                return False
        return True
