class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        freq = list(counter.values())
        freq.sort()
        
        ans, removed, half = 0, 0, math.ceil(len(arr)/2)
        while removed < half:
            ans += 1
            removed += freq.pop()
        return ans

    
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = {}
        for i in arr:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        freq = list(counter.values())
        freq.sort()
        
        ans, removed, half = 0, 0, math.ceil(len(arr)/2)
        while removed < half:
            ans += 1
            removed += freq.pop()
        return ans
