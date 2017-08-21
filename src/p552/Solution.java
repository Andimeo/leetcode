package p552;

class Solution {
	public int checkRecord(int n) {
		int mod = 1000000007;
		int dp[][][] = new int[3][3][2];
		dp[0][0][0] = 0;
		dp[0][0][1] = 1;
		dp[0][1][0] = 1;
		dp[0][1][1] = 0;
		dp[0][2][0] = 1;
		dp[0][2][1] = 0;
		int a = -2, b = -1, c = 0;
		for (int i = 1; i < n; i++) {
			a += 1;
			b += 1;
			c += 1;
			if (i > 1)
				a %= 3;
			b %= 3;
			c %= 3;

			dp[c][0][1] = (dp[b][1][0] + dp[b][2][0]) % mod;
			dp[c][1][0] = (dp[b][1][0] + dp[b][2][0]) % mod;
			dp[c][1][1] = (dp[b][0][1] + dp[b][1][1] + dp[b][2][1]) % mod;
			dp[c][2][0] = (dp[b][1][0] + (i == 1 ? 1 : dp[a][1][0])) % mod;
			dp[c][2][1] = (dp[b][0][1] + dp[b][1][1] + (i == 1 ? 0 : (dp[a][0][1] + dp[a][1][1]))) % mod;
		}
		return (dp[c][0][0] + dp[c][0][1] + dp[c][1][0] + dp[c][1][1] + dp[c][2][0] + dp[c][2][1]) % mod;
	}
}
