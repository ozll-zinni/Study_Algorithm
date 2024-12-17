/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    if (!root) return [];
    
    const result = [];
    const queue = [root];
    let leftToright = true;

    while(queue.length > 0){
        const levelsize = queue.length;
        const level = [];

        for (let i = 0; i < levelsize; i++) {
            const node = queue.shift();

            if (node === null) continue;

            if (leftToright) {
                level.push(node.val);
            } else {
                level.unshift(node.val);
            }

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        result.push(level);
        leftToright = !leftToright
    }

    return result
};