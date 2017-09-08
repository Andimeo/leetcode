public class Solution {
	public boolean isInterleave(String s1, String s2, String s3) {
		int n = s1.length();
		int m = s2.length();
		if(s3.length() != n + m)
			return false;
		boolean dp[][] = new boolean[n + 1][];
		for (int i = 0; i <= n; i++)
			dp[i] = new boolean[m + 1];
		dp[0][0] = true;
		for (int i = 1; i <= n; i++) {
			if (s1.charAt(i - 1) == s3.charAt(i - 1))
				dp[i][0] = true;
			else
				break;
		}
		for (int i = 1; i <= m; i++) {
			if (s2.charAt(i - 1) == s3.charAt(i - 1))
				dp[0][i] = true;
			else
				break;
		}
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (s3.charAt(i + j - 1) == s1.charAt(i - 1))
					dp[i][j] = dp[i][j] || dp[i - 1][j];
				if (s3.charAt(i + j - 1) == s2.charAt(j - 1))
					dp[i][j] = dp[i][j] || dp[i][j - 1];
			}
		}
		return dp[n][m];
	}
}