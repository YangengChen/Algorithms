package LeetCode.Java;
 
class Solution {
    public void flatten(TreeNode root) {
        flatten(root, null);
    }
    
    public TreeNode flatten(TreeNode root, TreeNode prev) {
        if(root == null) return prev;
        prev = flatten(root.right, prev);
        prev = flatten(root.left, prev);
        root.right = prev;
        root.left = null;
        return root;
    }

//   Definition for a binary tree node.
    public class TreeNode {
        int val;
        TreeNode left;
    TreeNode right;
        TreeNode(int x) { val = x; }
    }
}