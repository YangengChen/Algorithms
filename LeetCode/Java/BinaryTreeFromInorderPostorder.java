package LeetCode.Java;

import java.util.*;

class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
       if(inorder.length == 0 || postorder.length == 0) return null;
       Map<Integer, Integer> inMap = new HashMap<>();
       for(int i = 0; i < inorder.length; i++) inMap.put(inorder[i], i);
       return buildTree(0, inorder.length-1, postorder.length-1, inorder, postorder, inMap);
   }
   
   public TreeNode buildTree(int inStart, int inEnd, int postStart, int[] inorder, int[] postorder, Map<Integer,Integer> inMap) {
       if(postStart < 0 || inStart > inEnd) return null;
       TreeNode root = new TreeNode(postorder[postStart]);
       int inIndex = inMap.get(root.val);
       int numsRight = inEnd - inIndex;
       root.left = buildTree(inStart, inIndex-1, postStart-numsRight-1, inorder, postorder, inMap);
      root.right = buildTree(inIndex+1, inEnd, postStart-1, inorder, postorder, inMap);
       return root;
   }

   
//  Definition for a binary tree node.
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
 
}