var generateParenthesis = function(n) {
    const allParenthesis = []
    function dfs(l, r, memo=""){
        if(l!==0) {
            dfs(l-1, r, memo+"(")
        }
        if(l<r){
            dfs(l, r-1, memo+")")
        }
        if (l===0 && r===0){
            allParenthesis.push(memo)
        }
    }
    dfs(n,n)
    return allParenthesis
};

console.log(generateParenthesis(3))