/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    const result = [];
    let i = 0;
    const n = intervals.length;

    // 목표 구간과 겹치지 못하고 먼저 실행되는 구간
    while(i < n && intervals[i][1] < newInterval[0]) {
        result.push(intervals[i]);
        i++;
    }

    // 세 구간과 겹치는 구간들의 병합
    while(i < n && intervals[i][0] <= newInterval[1]){
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }

    result.push(newInterval);

    while (i < n) {
        result.push(intervals[i]);
        i++;
    }

    return result
};