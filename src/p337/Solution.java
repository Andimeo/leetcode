package p337;

import java.util.HashMap;
import java.util.Map;

class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
}

public class Solution {
	private Map<TreeNode, Integer> includedMap = new HashMap<>();
	private Map<TreeNode, Integer> nonIncludedMap = new HashMap<>();

	public int rob(TreeNode root) {
		return Math.max(DFS(root, true), DFS(root, false));
	}

	private int DFS(TreeNode root, boolean included) {
		if (root == null)
			return 0;
		if (included && includedMap.containsKey(root))
			return includedMap.get(root);
		if (!included && nonIncludedMap.containsKey(root))
			return nonIncludedMap.get(root);

		if (included) {
			includedMap.put(root, root.val + DFS(root.left, false) + DFS(root.right, false));
			return includedMap.get(root);
		}
		nonIncludedMap.put(root, Math.max(DFS(root.left, true), DFS(root.left, false))
				+ Math.max(DFS(root.right, true), DFS(root.right, false)));
		return nonIncludedMap.get(root);
	}
}
