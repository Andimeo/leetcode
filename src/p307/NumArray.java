package p307;

class SegmentTree {
	int nums[];
	int n;
	int tree[];
	int value[];
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
		value = new int[treeSize];
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
			value[node] = value[node + node + 1] + value[node + node + 2];
		} else
			value[node] = nums[left];
	}

	public void update(int index, int num) {
		update(0, index, num);
	}

	private int update(int node, int index, int num) {
		if (left[node] == right[node]) {
			int diff = num - value[node];
			value[node] = num;
			return diff;
		}
		int diff = 0;
		if (index <= ((left[node] + right[node]) >> 1))
			diff = update(node + node + 1, index, num);
		else
			diff = update(node + node + 2, index, num);
		value[node] += diff;
		return diff;
	}

	public int query(int l, int r) {
		return query(0, l, r);
	}

	private int query(int node, int l, int r) {
		if (l <= left[node] && r >= right[node])
			return value[node];
		if (l > right[node] || r < left[node])
			return 0;
		return query(node + node + 1, l, r) + query(node + node + 2, l, r);
	}
}

public class NumArray {
	private SegmentTree tree;

	public NumArray(int[] nums) {
		if (nums.length > 0)
			tree = new SegmentTree(nums);
	}

	void update(int i, int val) {
		if (tree == null)
			return;
		tree.update(i, val);
	}

	public int sumRange(int i, int j) {
		if (tree == null)
			return 0;
		return tree.query(i, j);
	}
}
