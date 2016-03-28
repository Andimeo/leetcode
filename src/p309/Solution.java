package p309;

public class Solution {
	public int maxProfit(int[] prices) {
		int n = prices.length;
		if (n < 2)
			return 0;
		int dp[][] = new int[2][n];
		for (int i = 1; i < n; i++) {
			dp[0][i] = Math.max(dp[0][i - 1], dp[1][i - 1]);
			if (i == 1)
				dp[1][i] = prices[i] - prices[0];
			else
				dp[1][i] = Math.max(dp[0][i - 2], dp[1][i - 1]) + prices[i] - prices[i - 1];
		}
		return Math.max(dp[0][n - 1], dp[1][n - 1]);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
