var canJump = function(nums) {
    let maxJump = 0
    for(let i=0; i<nums.length; i++) {
        if(i>maxJump) {
            return false
        }
        maxJump = Math.max(maxJump, i+nums[i])
        if(maxJump>=nums.length-1) {
            return true
        }
    }
};

console.log(canJump([2,3,1,1,4])) //true
console.log(canJump([3,2,1,0,4])) //false