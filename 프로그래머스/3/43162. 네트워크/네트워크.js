function solution(n, computers) {
    let visited = new Array(n).fill(false);
    var networkCnt = 0;
    
    function dfs(node) {
        visited[node] = true;
        for(let i = 0; i < n; i++) {
            if (computers[node][i] === 1 && !visited[i]){
                dfs(i);
            }
        }
    }
    
    for(let i = 0; i<n; i++){
        if(!visited[i]){
            dfs(i)
            networkCnt++
        }
    }
    return networkCnt;
}