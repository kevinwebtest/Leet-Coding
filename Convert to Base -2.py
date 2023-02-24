class Solution:
    def baseNeg2(self, n: int) -> str:
        if n==0:
            return "0"
        biner = ""
        while n:
            biner = str(n&1) + biner
            n = -(n>>1)
        return biner

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n==0:
            return "0"
        biner = ""
        while n:
            biner = str(n%2) + biner
            n = -(n//2)
        return biner

class Solution:
    def base2(self, n: int) -> str:
        if n==0:
            return "0"
        biner = ""
        while n:
            biner = str(n%2) + biner
            n = n//2
        return biner