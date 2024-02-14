/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const M = Math.floor(num/1000)
    num = Math.floor(num%1000)
    const D = Math.floor(num/500)
    num = Math.floor(num%500)
    const C = Math.floor(num/100)
    num = Math.floor(num%100)
    const L = Math.floor(num/50)
    num = Math.floor(num%50)
    const X = Math.floor(num/10)
    num = Math.floor(num%10)
    const V = Math.floor(num/5)
    num = Math.floor(num%5)
    const I = num
    let newRoman = "M".repeat(M) + "D".repeat(D) + "C".repeat(C) + "L".repeat(L) + "X".repeat(X) + "V".repeat(V) + "I".repeat(I)
    newRoman = newRoman.replace("DCCCC", "CM").replace("CCCC", "CD").replace("LXXXX", "XC").replace("XXXX", "XL").replace("VIIII", "IX").replace("IIII", "IV")
    return newRoman
};

console.log(intToRoman(1994)) // "MCMXCIV"