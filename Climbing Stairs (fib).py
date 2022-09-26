class Solution:
    def climbStairs(self, n: int) -> int:
        one, two= 1, 1
        for i in range(n-1): #change to n-2 for actual fib numbers
            temp = one
            one = one + two
            two = temp
        return one
    
    def fibbonaci(n):
        if n==1 or n==2:
            return 1
        fibList = [None for i in range(n+1)]
        fibList[1] = 1
        fibList[2] = 1
        for i in range(3,n+1):
            fibList[i] = fibList[i-1] + fibList[i-2]
        return fibList[n]
