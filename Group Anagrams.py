class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for s in strs:
            ssorted = "".join(sorted(s))
            if ssorted in memo:
                memo[ssorted] = memo[ssorted] + [s]
            else:
                memo[ssorted] = [s]
        return [x for x in memo.values()]
