function shortestSumComb(target, numbers, memo={}){
  if (target in memo)
    return memo[target];
  if (target===0)
    return [];
  if (target<0)
    return null;

  let shortestComb = null;
  for (let num of numbers){
    const remainder = target - num;
    let currentComb = shortestSumComb(remainder, numbers, memo);
    memo[remainder] = currentComb
    if (currentComb !== null){
      currentComb = [...currentComb,num];
      if (shortestComb===null || currentComb.length<shortestComb.length)
        shortestComb = currentComb;
    }
  }
//   memo[target] = shortestComb;
  return shortestComb;
}

console.log(shortestSumComb(7,[2,3]))
console.log(shortestSumComb(7,[5,3,4,7])) 
console.log(shortestSumComb(8,[1,4,5]))
console.log(shortestSumComb(7,[4,2]))
console.log(shortestSumComb(300,[14,7,15])) 
