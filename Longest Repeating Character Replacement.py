class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count_ch = {}
        maxreplace = 0
        for r in range(len(s)):
            if s[r] not in count_ch:
                count_ch[s[r]] = 0
            count_ch[s[r]] += 1

            window = r-l+1
            if window - max(count_ch.values()) <= k:
                maxreplace = max(maxreplace, window)

            else:
                count_ch[s[l]] -= 1
                l+=1
        return maxreplace