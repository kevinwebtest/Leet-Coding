class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while (b & mask)>0:
            carry = (a&b)<<1
            a ^= b
            b = carry
        if b>0:
            return a&mask
        else:
            return a

yo = Solution()
print(yo.getSum(2,-5))
