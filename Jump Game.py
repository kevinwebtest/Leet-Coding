class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump=0
        for i in range(len(nums)):
            if i>maxJump:
                return False
            maxJump = max(maxJump, i + nums[i])
            if maxJump>=len(nums)-1:
                return True
        return True