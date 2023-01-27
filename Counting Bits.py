# Brute Force
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n+1)]
      
# DP
class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        for i in range(1,n+1):
            output.append(output[i//2]+i%2)
        return output

# Brute Force
class Solution:
    def countBits(self, n: int) -> List[int]:
        output= []
        for i in range(n+1):
            binary = bin(i).replace("0b","")
            count=0
            for biner in binary:
                if biner == '1':
                    count+=1
            output.append(count)
        return output