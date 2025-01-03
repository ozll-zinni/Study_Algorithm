/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let n = nums.length;
    let prod = new Array(n).fill(1);

    let left = 1;
    for(let i = 0; i < n; i++){
        prod[i] = left;
        left *= nums[i];
    }
    
    let right = 1;
    for (let i = n - 1; i >= 0; i--) {
        prod[i] *= right;
        right *= nums[i]
    }
    return prod;
};