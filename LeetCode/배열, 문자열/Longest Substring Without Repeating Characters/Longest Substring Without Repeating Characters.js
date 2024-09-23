/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let wordexist = new Map();
    let start = 0;
    let maxlength = 0;

    for(let i = 0; i < s.length; i++) {
        let char = s[i];
        
        if (wordexist.has(char) && wordexist.get(char) >= start){
            start = wordexist.get(char) + 1;
        }

        wordexist.set(char, i);
        maxlength = Math.max(maxlength, i - start + 1);

    }
    return maxlength
};
