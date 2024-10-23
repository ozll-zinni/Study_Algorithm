/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hash_map = {}

    for(let i = 0; i < nums.length; i++) {
        let num = nums[i];
        let diff = target - num;

        if (diff in hash_map) {
            return [hash_map[diff],i];
        }
        hash_map[num] = i;
    }
};