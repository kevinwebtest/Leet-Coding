var rob = function(nums) {
    function robDFS(numsSlice, i, memo) {
        if (i in memo) {
            return memo[i];
        }
        if (i<numsSlice.length){
            memo[i] = Math.max(numsSlice[i]+robDFS(numsSlice, i+2, memo), robDFS(numsSlice, i+1, memo));
            return memo[i];
        }
        return 0;
    }
    if (nums.length===0) return 0;
    else if (nums.length===1) return nums[0];
    else{
        front = nums.slice(0,nums.length-1);
        back = nums.slice(1,nums.length);
        return Math.max(robDFS(front, 0, {}), robDFS(back, 0, {}));
    }
};