class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        output = []
        def DFS(digit, n):
            if n == 0:
                return output.append(digit)
            
            single = digit % 10
            next_digits = set([single + k, single - k])
            for next_digit in next_digits:
                if 0<=next_digit<10:
                    numbers = digit*10 + next_digit
                    DFS(numbers, n-1)
            
        for digit in range(1,10):
            DFS(digit, n-1)
        
        return output
