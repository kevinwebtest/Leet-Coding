import math
def getMinCost(val, t_nodes, t_from, t_to):
    for i in range(len(val)):
        val[i] %= 2

    adj = [[] for _ in range(t_nodes)]
    for i in range(len(t_from)):
        u, v = t_from[i] - 1, t_to[i] - 1
        adj[u].append(v)
        adj[v].append(u)

    def merge(dp1, dp2):
        res = [math.inf for _ in range(2)]
        res[0] = min(dp1[0] + dp2[0], dp1[1] + dp2[1] + 1)
        res[1] = min(dp1[0] + dp2[1] + 1, dp1[1] + dp2[0])
        return res

    dp = [[math.inf for _ in range(2)] for _ in range(t_nodes)]
    def dfs(u, p):
        dp[u][val[u]] = 0

        for i in adj[u]:
            if i == p:
                continue
            dfs(i, u)
            dp[u] = merge(dp[u], dp[i])

    dfs(0, -1)
    return dp[0][0]
print(getMinCost([2,1,1], 3, [1,1], [2,3]))
print(getMinCost([3, 2, 4, 2, 5], 5, [1, 1, 3, 5],  [2, 3, 4, 5]))
