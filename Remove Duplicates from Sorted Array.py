class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        out = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1] :
                out += 1
                nums[out] = nums[i+1]
                
        return out+1
