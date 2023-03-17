# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return i,j
class Solution:
    def twoSum(self, nums, target: int):
        memo = {}
        for i in range(len(nums)):
            remainder = target-nums[i]
            if remainder in memo:
                return [memo[remainder],i]
            else:
                memo[nums[i]] = i

sol = Solution()
print(sol.twoSum([1,3,4,2,5], 7))

