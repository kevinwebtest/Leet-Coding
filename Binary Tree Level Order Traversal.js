var levelOrder = function(root, output=[], order=0) {
    if (!root) return [];
    if (output.length<=order) {
        output.push([]);
    }
    output[order].push(root.val);
    levelOrder(root.left,output,order+1);
    levelOrder(root.right,output,order+1);
    return output;
};