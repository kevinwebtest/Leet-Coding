class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
    
        # Create a list to store the minimum cost to reach each step
        dp = [0] * n
        
        # Base cases
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Compute the minimum cost for each step starting from the third step
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # The minimum cost to reach the top floor will be the minimum of the last two steps' costs
        return min(dp[n-1], dp[n-2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(n):
            if n<2:
                return cost[n]
            return cost[n] + min(dp(n-1), dp(n-2))
        return min(dp(len(cost)-1), dp(len(cost)-2))