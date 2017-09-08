public class Solution {
	public int numDistinct(String S, String T) {
		int n = S.length(), m = T.length();
		int dp[][] = new int[n][];
		for (int i = 0; i < n; i++)
			dp[i] = new int[m];

		for (int i = 0; i < n; i++)
			if (S.charAt(i) == T.charAt(0))
				dp[i][0] = 1;

		for (int i = 1; i < m; i++) {
			int count = 0;
			for (int j = 0; j < n; j++) {
				if (S.charAt(j) == T.charAt(i))
					dp[j][i] += count;
				if (S.charAt(j) == T.charAt(i - 1))
					count += dp[j][i - 1];
			}
		}

		int res = 0;
		for (int i = 0; i < n; i++)
			res += dp[i][m - 1];
		return res;
	}

	public static void main(String[] args) {
		System.out.println(new Solution().numDistinct("rabbbit", "rabbit"));
	}
}