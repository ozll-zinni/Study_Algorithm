/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    var maxSum = -10000
    var currSum = 0;

    for (let num of nums){
        currSum = Math.max(num, currSum + num);
        maxSum = Math.max(maxSum, currSum)
    };
    return maxSum;
};