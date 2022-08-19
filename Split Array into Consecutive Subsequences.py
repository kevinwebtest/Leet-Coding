class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = Counter(nums)
        end = Counter()
        for i in nums:
            if not left[i]: 
                continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
                print(end[i])
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
                print(end[i])
            else:
                return False
        return True
