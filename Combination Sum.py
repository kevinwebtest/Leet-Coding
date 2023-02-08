class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        allComb = []
        candidates.sort()
        def dfs(idx, target, comb):
            if target==0:
                allComb.append(comb)
            for i in range(idx,len(candidates)):
                if target>=candidates[i]:
                    dfs(i, target - candidates[i], comb+[candidates[i]])
    
        dfs(0, target, [])
        return allComb
    