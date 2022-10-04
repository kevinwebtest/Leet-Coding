class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
        for i in range(count):
            nums.remove(0) 
            nums.append(0)
            
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i]!=0 and nums[zero]==0:
                nums[i],nums[zero] = nums[zero],nums[i]
            if nums[zero]!=0:
                zero+=1
