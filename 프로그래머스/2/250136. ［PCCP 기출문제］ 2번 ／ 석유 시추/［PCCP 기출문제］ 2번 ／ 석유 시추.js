function solution(land) {
    const n = land.length;
    const m = land[0].length;
    
    const visited = Array.from({ length: n }, () => Array(m).fill(false));

    
    const components = [];
    
    function bfs(startR, startC) {
        const queue = [[startR, startC]];
        visited[startR][startC]  = true;
        
        let size = 0;
        const columnsTouched = new Set();        
        
        while(queue.length) {
            const [r,c] = queue.shift();
            size++;
            columnsTouched.add(c);
            
            const dr = [1, -1, 0, 0];
            const dc = [0, 0, 1, -1];
            for (let i = 0; i < 4; i++) {
                const nr = r + dr[i];
                const nc = c + dc[i];
                if (
                    nr >= 0 && nr < n && 
                    nc >= 0 && nc < m && 
                    land[nr][nc] === 1 && 
                    !visited[nr][nc]
                ) {
                    visited[nr][nc] = true;
                    queue.push([nr, nc]);
                }
            }
        }
        return {size, columns: columnsTouched};
    }
    
    for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (land[i][j] === 1 && !visited[i][j]) {
        const component = bfs(i, j);
        components.push(component);
      }
    }
  }
    const colSum = Array(m).fill(0);
  for (const comp of components) {
    const { size, columns } = comp;
    for (const c of columns) {
      colSum[c] += size;
    }
  }
    return Math.max(...colSum);
}