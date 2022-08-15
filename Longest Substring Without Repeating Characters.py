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
