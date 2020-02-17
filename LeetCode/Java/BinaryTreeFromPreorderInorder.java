package LeetCode.Java;

import java.util.*;

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(preorder.length == 0|| inorder.length == 0) return null;
        Map<Integer, Integer> inMap = new HashMap<>();
        for(int i = 0; i < inorder.length; i++) inMap.put(inorder[i], i);
        return buildTree(0, 0, inorder.length-1, preorder, inorder, inMap);
    }
    
    public TreeNode buildTree(int preStart, int inStart, int inEnd, int[] preorder, int[] inorder, Map<Integer,Integer> inMap) {
        if(preStart > preorder.length-1 || inStart > inEnd) return null;
        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = inMap.get(root.val);
        int numsLeft = inIndex - inStart;
        root.left = buildTree(preStart+1, inStart, inIndex-1, preorder, inorder, inMap);
       root.right = buildTree(preStart+numsLeft+1, inIndex+1, inEnd, preorder, inorder, inMap);
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