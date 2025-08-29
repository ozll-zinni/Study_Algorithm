function solution(n, w, num) {
    let boxArr = Array.from({length:w}, () => []);
    let numIdx = [];
    
    for(let i = 0; i < n; i ++){
        let arrIdx = i % w;
        if(Math.floor(i/w) % 2 == 0){
            boxArr[arrIdx].push(i+1);
        } else {
            boxArr[w-1-arrIdx].push(i+1);
        }
    
        if(num == i+1){
            numIdx = (Math.floor(i/w) % 2 == 0)? [arrIdx, boxArr[arrIdx].length-1] : [w-1-arrIdx, boxArr[w-1-arrIdx].length-1];
        }
    }
    
    return boxArr[numIdx[0]].length - numIdx[1];
}