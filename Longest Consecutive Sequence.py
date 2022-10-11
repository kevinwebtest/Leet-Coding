class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        nums.sort()
        longestSort = 1
        increment = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                increment.append(nums[i])
                if len(increment)>longestSort:
                    longestSort = len(increment)
            elif nums[i-1]==nums[i]:
                continue
            else:
                increment = [nums[i]]
        return longestSort
