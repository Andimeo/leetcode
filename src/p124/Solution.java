public class Solution {
	private int max = Integer.MIN_VALUE;
	public int maxPathSum(TreeNode root) {
		ok(root);
		return max;
	}
	private int ok(TreeNode root) {
		if(root == null) return 0;
		int left = ok(root.left);
		int right = ok(root.right);
		int sum = root.val;
		sum += left > 0 ? left : 0;
		sum += right > 0 ? right : 0;
		if(sum > max) max = sum;
		return Math.max(root.val, Math.max(root.val + left, root.val + right));
	}
}