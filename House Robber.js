var rob = function(nums) {
    let twoStepsBack = 0
    let oneStepBack = 0
    for (let num of nums) {
        let biggest = Math.max(twoStepsBack + num, oneStepBack)
        twoStepsBack = oneStepBack
        oneStepBack = biggest
    }
    return biggest
};


var rob = function(nums, i=0, memo={}) {
    if (i in memo) {
        return memo[i]
    }
    if (nums.length > i) {
        memo[i] = Math.max(nums[i] + rob(nums, i+2, memo), rob(nums, i+1, memo))
        return memo[i]
    } 
    return 0
};