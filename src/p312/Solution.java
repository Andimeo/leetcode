package p312;

public class Solution {
	public int maxCoins(int[] nums) {
		int n = nums.length;
		int nNums[] = new int[n + 2];
		nNums[0] = nNums[n + 1] = 1;
		for (int i = 1; i <= n; i++)
			nNums[i] = nums[i - 1];

		int dp[][] = new int[n + 2][n + 2];
		dp[0][0] = dp[n + 1][n + 1] = 0;

		for (int len = 1; len <= n; len++) {
			for (int i = 1; i <= n - len + 1; i++) {
				int end = i + len - 1;
				for (int j = i; j <= end; j++) {
					int value = (j > i ? dp[i][j - 1] : 0) + (j < end ? dp[j + 1][end] : 0)
							+ nNums[i - 1] * nNums[j] * nNums[end + 1];
					if (value > dp[i][end])
						dp[i][end] = value;
				}
			}
		}
		return dp[1][n];
	}

	public static void main(String[] args) {
		int nums[] = { 2,3 };
		System.out.println(new Solution().maxCoins(nums));
	}

}
