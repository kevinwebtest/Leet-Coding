class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        newposition = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target > nums[i]:
                newposition = i+1
        return newposition
