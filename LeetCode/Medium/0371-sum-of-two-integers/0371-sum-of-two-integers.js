/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    while (b !== 0){
        a += Math.sign(b);
        b -= Math.sign(b);
    }
    return a
};