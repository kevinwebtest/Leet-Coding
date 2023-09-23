/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const allComb = []
    function dfs(newComb, idx){
      allComb.push(newComb)
      for(let i=idx; i<nums.length; i++) {
        dfs([...newComb, nums[i]], i+1)
      }
  
    }
    dfs([], 0)
    return allComb
  };