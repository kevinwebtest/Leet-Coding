class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                i = magazine.index(c)
                magazine = magazine[:i] + magazine[i+1:]
        return True
