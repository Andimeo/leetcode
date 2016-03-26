package p315;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class SegmentTree {
	int nums[];
	int n;
	int tree[];
	int count[];
	int left[];
	int right[];

	public SegmentTree(int nums[]) {
		this.nums = nums;
		this.n = nums.length;
		buildTree();
	}

	public void buildTree() {
		int treeSize = (n << 2) + 4;
		tree = new int[treeSize];
		count = new int[treeSize];
		left = new int[treeSize];
		right = new int[treeSize];
		buildTree(0, 0, n - 1);
	}

	private void buildTree(int node, int left, int right) {
		this.left[node] = left;
		this.right[node] = right;
		if (left != right) {
			int mid = ((left + right) >> 1);
			buildTree(node + node + 1, left, mid);
			buildTree(node + node + 2, mid + 1, right);
		}
	}

	public void addNumber(int num) {
		addNumber(0, num);
	}

	private void addNumber(int node, int num) {
		count[node]++;
		if (left[node] == right[node])
			return;
		if (num <= nums[(left[node] + right[node]) >> 1])
			addNumber(node + node + 1, num);
		else
			addNumber(node + node + 2, num);
	}

	public int query(int num) {
		return query(0, num);
	}

	private int query(int node, int num) {
		if (nums[right[node]] < num)
			return count[node];
		if (nums[left[node]] >= num)
			return 0;
		return query(node + node + 1, num) + query(node + node + 2, num);
	}
}

public class Solution {
	public List<Integer> countSmaller(int[] nums) {
		if (nums.length == 0) {
			return Collections.emptyList();
		}
		int sortedNums[] = Arrays.copyOf(nums, nums.length);
		Arrays.sort(sortedNums);
		SegmentTree tree = new SegmentTree(sortedNums);
		List<Integer> list = new ArrayList<Integer>();
		for (int i = nums.length - 1; i >= 0; i--) {
			list.add(tree.query(nums[i]));
			tree.addNumber(nums[i]);
		}
		Collections.reverse(list);
		return list;
	}

	public static void main(String[] args) {
		int nums[] = { 1, 1 };
		for (int t : new Solution().countSmaller(nums)) {
			System.out.println(t);
		}
	}

}
