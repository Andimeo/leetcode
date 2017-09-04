package p403;

public class Solution {
	interface Predicate<T> {
		boolean test(T a, T b);
	};

	int bisect(int[] nums, int value, Predicate<Integer> p) {
		int low = 0, high = nums.length;
		int result = high;
		while (low < high) {
			int mid = (low + high) >> 1;
			if (p.test(nums[mid], value)) {
				result = mid;
				high = mid;
			} else {
				low = mid + 1;
			}
		}
		return result;
	}

	int bisect_left(int[] nums, int value) {
		return bisect(nums, value, (a, b) -> (a >= b));
	}

	int bisect_right(int[] nums, int value) {
		return bisect(nums, value, (a, b) -> (a > b));
	}

	public boolean canCross(int[] stones) {
		if (stones[1] != 1)
			return false;
		int n = stones.length;
		int dp[][] = new int[n][n];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				dp[i][j] = -1;
		dp[1][1] = 0;

		for (int i = 1; i < n; i++) {
			for (int j = 1; j < n; j++) {
				if (dp[i][j] != -1) {
					int step_min = Math.max(1, j - 1);
					int step_max = j + 1;
					int pos_left = bisect_left(stones, stones[i] + step_min);
					int pos_right = bisect_right(stones, stones[i] + step_max);
					for (int p = pos_left; p < pos_right; p++) {
						int steps = stones[p] - stones[i];
						dp[p][steps] = i;
					}
				}
			}
		}
		for (int i = 1; i < n; i++) {
			if (dp[n - 1][i] != -1)
				return true;
		}
		return false;
	}
}
