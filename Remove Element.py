class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=len(nums)-1
        i=0
        while i<j:
            if nums[i]==val and nums[j]!=val:
                nums[i],nums[j] = nums[j], nums[i]
            elif nums[j]==val:
                j-=1
            else:
                i+=1
        while val in nums:
            nums.pop()

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
            
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
