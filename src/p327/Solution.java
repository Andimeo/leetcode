package p327;

import java.util.Arrays;

class SegmentTree {
	long nums[];
	int n;
	int tree[];
	int count[];
	int left[];
	int right[];

	public SegmentTree(long nums[]) {
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

	public void addNumber(long num) {
		addNumber(0, num);
	}

	private void addNumber(int node, long num) {
		count[node]++;
		if (left[node] == right[node])
			return;
		if (num <= nums[(left[node] + right[node]) >> 1])
			addNumber(node + node + 1, num);
		else
			addNumber(node + node + 2, num);
	}

	public int query(long lower, long upper) {
		return query(0, lower, upper);
	}

	private int query(int node, long lower, long upper) {
		if (nums[right[node]] <= upper && nums[left[node]] >= lower)
			return count[node];
		if (nums[right[node]] < lower || nums[left[node]] > upper)
			return 0;
		return query(node + node + 1, lower, upper) + query(node + node + 2, lower, upper);
	}
}

public class Solution {
	public int countRangeSum(int[] nums, int lower, int upper) {
		if(nums.length == 0)
			return 0;
		long sums[] = new long[nums.length + 1];
		sums[0] = nums[0];
		sums[nums.length] = 0;
		for (int i = 1; i < nums.length; i++)
			sums[i] = sums[i - 1] + nums[i];
		long[] sortedSums = Arrays.copyOf(sums, sums.length);
		Arrays.sort(sortedSums);
		SegmentTree tree = new SegmentTree(sortedSums);
		int ans = 0;
		tree.addNumber(0);
		for (int i = 0; i < nums.length; i++) {
			ans += tree.query(sums[i] - upper, sums[i] - lower);
//			System.out.println(ans);
			tree.addNumber(sums[i]);
		}
		return ans;
	}
/*
 * [2147483647,-2147483648,-1,0]
-1
0
[-4,0,-3,-1,1,2,1,-4]
0
6
 */
	public static void main(String[] args) {
		int array[] = { -4,0,-3,-1,1,2,1,-4 };
		System.out.println(new Solution().countRangeSum(array, 0, 6));
	}
}
