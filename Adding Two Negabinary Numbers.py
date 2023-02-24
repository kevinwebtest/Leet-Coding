class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num1=0
        num2=0
        for i, biner in enumerate(reversed(arr1)):
            if biner==1:
                num1 += (-2)**i
        for i, biner in enumerate(reversed(arr2)):
            if biner==1:
                num2 += (-2)**i
        summed = num1+num2
        summedlist=[]
        while summed:
            summedlist.append(summed&1)
            summed = -(summed>>1)
        summedlist.reverse()
        return summedlist if summedlist else [0]