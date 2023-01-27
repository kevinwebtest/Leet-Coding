class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = self.toBinary(n)
        count=0

        for i in binary:
            if i=='1':
                count +=1

        return count


    def toBinary(self, num, biner=""):
        if num>1:
            biner = self.toBinary(num//2,biner)
        biner += str(num%2)
        return biner

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n).replace("0bx","")
        count=0

        for i in binary:
            if i=='1':
                count +=1

        return count