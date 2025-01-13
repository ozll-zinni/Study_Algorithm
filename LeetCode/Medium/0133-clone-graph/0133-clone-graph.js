/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {

    var visited = {}

    let dfs = function(node) {
        if(!node){
            return node;
        }

        if(visited[node.val]!=null){
            return visited[node.val]
        }

        let root = new Node(node.val);
        
        visited[node.val] = root;

        for(let n of node.neighbors) {
            root.neighbors.push(dfs(n))
        }
        return root
    }
    return dfs(node)
};