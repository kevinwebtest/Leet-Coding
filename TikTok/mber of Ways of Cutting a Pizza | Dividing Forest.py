class Solution:
    def ways(self, pizza: List[str], K: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        presum = [[0]*(n+1) for _ in range(m+1)]
        memo = {}

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                presum[i][j] = presum[i+1][j] + presum[i][j+1] - presum[i+1][j+1] + \
                (1 if pizza[i][j]=='A' else 0)

        def dfs(cur_i, cur_j, k):
            if (cur_i,cur_j, k) in memo:
                return memo[(cur_i,cur_j, k)]
            if presum[cur_i][cur_j]==0:
                return 0
            if k==0:
                return 1

            count = 0
            for i in range(cur_i+1, m):
                if presum[cur_i][cur_j]-presum[i][cur_j]>0:
                    count += dfs(i, cur_j, k-1)
            for j in range(cur_j+1, n):
                if presum[cur_i][cur_j]-presum[cur_i][j]>0:
                    count += dfs(cur_i, j, k-1)
            memo[(cur_i,cur_j, k)] = count
            return count
        
        return dfs(0,0,K-1) % (10**9+7)
