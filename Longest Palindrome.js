var longestPalindrome = function(s) {
    const countDict = {}
    for (let i=0;i<s.length;i++) {
        if (s[i] in countDict) {
            countDict[s[i]] += 1
        } else {
            countDict[s[i]] = 1
        }
    }
    length= 0
    let haveone = false
    for (let i in countDict) {
        if (countDict[i]!==1) {
            if (countDict[i]%2===1) {
                countDict[i]-=1
                haveone = true
            }
            length+=countDict[i]
        } else {
            haveone = true
        }
    }
    return length+(haveone? 1:0)
};