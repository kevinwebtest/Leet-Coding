class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        memo = {}
        for n1 in range(len(nums)):
            prod=1
            if nums[n1] in memo:
                output.append(output[memo[nums[n1]]])
                continue
            for n2 in range(len(nums)):
                if n1!=n2:
                    prod*=nums[n2]
                
            memo[nums[n1]]=n1
            output.append(prod)
        return output
