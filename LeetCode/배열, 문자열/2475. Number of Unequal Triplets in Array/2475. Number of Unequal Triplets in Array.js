/**
 * @param {number[]} nums
 * @return {number}
 */
var unequalTriplets = function(nums) {
    const long = nums.length;
    let answer = 0;

    for(let i = 0; i < long-2; i++){
        for(let j = i+1; j < long - 1; j++) {
            if (nums[i] !== nums[j]) {
                for (let k = j + 1; k < long; k++) {
                    if(nums[k] !== nums[i] && nums[k] !== nums[j]) answer++;
                }
            }
        }
    }
    return answer;
};