function solution(players, m, k) {
    let server = Array(24).fill(0);
    let answer = 0;
    
    players.forEach((playerCnt, sTime) => {
        if(parseInt(playerCnt/m) > server[sTime]) {
            let needServerCnt = parseInt(playerCnt/m) - server[sTime];
            for(let i = 0; i<k; i++) {
                if(sTime + i <=23){
                    server[sTime + i] = server[sTime + i] + needServerCnt;
                }
            }
            
            answer += needServerCnt;
        }
    })
    return answer;
}