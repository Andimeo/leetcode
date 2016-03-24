package p327;

public class Solution {
	public int countRangeSum(int[] nums, int lower, int upper) {
		int sum[] = new int[nums.length + 1], ans = 0;
		for (int i = 0; i < nums.length; i++)
			sum[i + 1] = sum[i] + nums[i];
		for (int i = 1; i <= nums.length; i++) {
			int l = lowerBound(sum, 0, i, sum[i] - upper);
			int r = upperBound(sum, 0, i, sum[i] - lower);
			if (l != -1 && r != -1) {
				ans += r - l + 1;
			}
		}
		return ans;
	}

	private int lowerBound(int array[], int l, int r, int value) {
		int left = l, right = r;
		int ans = -1;
		while (left < right) {
			int mid = ((left + right) >> 1);
			if (array[mid] < value) {
				left = mid + 1;
			} else {
				right = mid;
				ans = mid;
			}
		}
		return ans;
	}

	private int upperBound(int array[], int l, int r, int value) {
		int left = l, right = r;
		int ans = -1;
		while (left < right) {
			int mid = ((left + right) >> 1);
			if (array[mid] <= value) {
				left = mid + 1;
				ans = mid;
			} else {
				right = mid;
			}
		}
		return ans;
	}

	public static void main(String[] args) {
		int array[] = { -2, 5, -1 };
		System.out.println(new Solution().countRangeSum(array, -2, 2));
	}
}
