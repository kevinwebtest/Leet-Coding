class Solution(object):
    def mySqrt(self, x):
        left, right = 0 , x
        while True:
            mid = left + (right-left)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid*mid:
                right = mid - 1
            else:
                left = mid + 1
