var threeSum = function(nums) {
    nums.sort(function(a, b){return a-b})
    function twoSum(newNums, curr) {
        let i = 0
        let j = newNums.length-1
        while(i<j) {
            const summed = curr+newNums[i]+newNums[j]
            if (summed>0) {
                j-=1
            } else if (summed<0) {
                i+=1
            } else {
                output.push([curr, newNums[i], newNums[j]])
                while(newNums[i+1]===newNums[i]) i+=1
                while(newNums[j-1]===newNums[j]) j-=1
                i+=1
                j-=1
            }
        }
    }
    const output = []
    for(let i=0; i<nums.length-2; i++) {
        if(nums[i]>0) break
        if(i>0 && nums[i]===nums[i-1]) continue
        let newNums = nums.slice(i+1,nums.length)
        twoSum(newNums, nums[i])
    }
    return output
};