class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        for num in nums:
            if num in memo:
                memo[num] += 1
            else:
                memo[num] = 1
        memo = sorted(memo, key=memo.get, reverse=True)
        return [mf for mf in memo[:k]]
