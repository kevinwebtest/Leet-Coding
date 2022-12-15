class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        maxLength = start = 0
        for i, ch in enumerate(s):
            if ch in char and char[ch] >= start:
                start = char[ch] + 1
            else:
                maxLength = max(maxLength, i-start+1)
            char[ch] = i
        return maxLength

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        substring = ""
        for i in range(len(s)):
            if s[i] not in substring:
                substring += s[i]
            else:
                idx = substring.index(s[i])
                substring = substring[idx+1:] + s[i]
            if len(substring) > len(longest):
                longest = substring
        return len(longest)
