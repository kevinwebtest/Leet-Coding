class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n).replace('0b','')
        output = ""
        while len(binary) < 32:
            binary = '0' + binary
        for i in binary:
            output = i + output
        return int(output,2)