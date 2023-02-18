class Solution:
    def generate(self, numRows: int):
        triangle = [[1]*i for i in range(1,numRows+1)]
        for i in range(1, numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle

sol = Solution()
print(sol.generate(5))
