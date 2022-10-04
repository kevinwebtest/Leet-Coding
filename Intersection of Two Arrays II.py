class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        samenums = []
        for x in range(len(nums1)):
            if nums1[x] in nums2:
                i = nums2.index(nums1[x])
                temp = nums2.pop(i)
                samenums.append(temp)
        return samenums
      
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        samenums = []
        nums1.sort()
        nums2.sort()
        i,j=0,0
        while len(nums1)>i and len(nums2)>j:
            if nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                samenums.append(nums1[i])
                i+=1
                j+=1
        return samenums
