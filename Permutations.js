/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const numslist = []
    function dfs(newComb) {
        if (newComb.length===nums.length) {
            numslist.push([...newComb])
            return
        }
        for(let i=0; i<nums.length; i++) {
            console.log(i, newComb)
            if (newComb.includes(nums[i])) {
                continue
            }
            newComb.push(nums[i])
            dfs([...newComb])
            newComb.pop()
        }
    }
    dfs([])
    return numslist
};

//or better
var permute = function(nums) {
    const allComb = []
    dfs(nums, [], allComb)
    return allComb
};

function dfs(nums, newComb, allComb) {
    if (nums.length===0) {
        allComb.push(newComb)
    } 
    for (let i=0;i<nums.length;i++) {
        dfs(nums.slice(0, i).concat(nums.slice(i+1, nums.length)), [...newComb, nums[i]], allComb)
    }
}