package p213;

import java.util.Arrays;

public class Solution {
	private int rob2(int[] nums) {
		int dp[][] = new int[nums.length + 1][2];
		dp[0][0] = dp[0][1] = 0;

		for (int i = 0; i < nums.length; i++) {
			dp[i + 1][0] = Math.max(dp[i][0], dp[i][1]);
			dp[i + 1][1] = dp[i][0] + nums[i];
		}
		return Math.max(dp[nums.length][0], dp[nums.length][1]);
	}

	public int rob(int[] nums) {
		if(nums.length == 0)
			return 0;
		if(nums.length == 1)
			return nums[0];
		return Math.max(rob2(Arrays.copyOfRange(nums, 0, nums.length - 1)), rob2(Arrays.copyOfRange(nums, 1, nums.length)));
	}

	public static void main(String[] args) {
		System.out.println(new Solution().rob(new int[] {1}));
	}
}
