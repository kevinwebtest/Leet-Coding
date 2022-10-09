class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        df = [0]+[float('inf')]*amount 
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    df[i] = min(df[i],df[i-coin]+1)
        if df[-1] == float('inf'):
            return -1
        return df[-1]
