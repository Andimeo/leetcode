/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode sortedArrayToBST(int[] num) {
        return sorted(num, 0, num.length);
    }
    private TreeNode sorted(int []num, int s, int e) {
        if(s >= e)
            return null;
        int mid = (s+e)>>1;
        TreeNode root = new TreeNode(num[mid]);
        root.left = sorted(num, s, mid);
        root.right = sorted(num, mid+1, e);
        return root;
    }
}