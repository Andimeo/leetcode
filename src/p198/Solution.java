package p198;

public class Solution {
	public int rob(int[] nums) {
		int dp[][] = new int[nums.length + 1][2];
		dp[0][0] = dp[0][1] = 0;
		
		for(int i = 0; i < nums.length; i++) {
			dp[i+1][0] = Math.max(dp[i][0], dp[i][1]);
			dp[i+1][1] = dp[i][0] + nums[i];
		}
		return Math.max(dp[nums.length][0], dp[nums.length][1]);
	}
}
