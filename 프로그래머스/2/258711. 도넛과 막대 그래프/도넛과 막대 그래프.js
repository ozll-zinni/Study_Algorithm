function solution(edges) {
    let start = null
    
    let bar = 0
    let donut = 0
    let character8 = 0
    const graph = []

    for (const [from, to] of edges) {
        if (!graph[from]) {
            graph[from] = {
                from: [],
                to: [to],
                val: from
            }
        } else graph[from].to.push(to)
        if (!graph[to]) {
            graph[to] = {
                from: [from],
                to: [],
                val: to
            }
        } else graph[to].from.push(from)
    }
    graph.shift()
    for(const node of graph) {
        if (!node) continue;
        const toLen = node.to.length
        const fromLen = node.from.length
        
        if(toLen === 0) bar++
        else if(toLen === 2) {
            if(fromLen > 0) character8++
            else start = node
        }
        else if(toLen >= 2) start = node
    }
    donut = start.to.length - bar - character8
    return [start.val, donut, bar, character8] 
}