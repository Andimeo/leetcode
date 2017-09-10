public class Solution {
	public int longestValidParentheses(String s) {
		int[] dp = new int[s.length()];
		int res = 0;
		for(int i = 1; i < s.length(); i++) {
			char c = s.charAt(i);
			if(c != ')')
				continue;
			int lc = s.charAt(i-1);
			if(lc == '(')
				dp[i] = (i > 1 ? dp[i-2] + 2 : 2);
			else {
				if(i - 1 - dp[i-1] >= 0 && s.charAt(i - 1 - dp[i-1]) == '(')
					dp[i] = dp[i-1] + 2 + (i - 2 - dp[i-1] >= 0 ? dp[i-2-dp[i-1]] : 0);
			}
			res = Math.max(res, dp[i]);
		}
		return res;
	}

	public static void main(String[] args) {
		System.out.println(new Solution().longestValidParentheses(")(((((()())()()))()(()))("));
	}
}