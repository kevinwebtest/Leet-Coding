/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let memo = ""
    for(let i=0;i<haystack.length;i++) {
        if (haystack[i]===needle[0] && i+needle.length<=haystack.length) {
            memo = haystack.slice(i, i+needle.length)
            if (memo===needle) {
                return i
            }
        }
    }
    return -1
};
