var coinChange = function(coins, amount) {
    const dfs = (target, memo={}) => {
        if(target in memo) return memo[target]
        if(target<0) return -1
        else if (target===0) return 0
        let smallestCount = Infinity
        for(let i=0; i<coins.length; i++) {
            let count = dfs(target-coins[i], memo)
            if (count>=0 && count<smallestCount) {
                smallestCount = count + 1
            }
        }
        memo[target] = smallestCount === Infinity ? -1 : smallestCount
        return memo[target]
    }
    return dfs(amount)
};

console.log(coinChange([1,2,5], 11))