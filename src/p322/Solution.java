package p322;

import java.util.Arrays;

public class Solution {
    public int coinChange(int[] coins, int amount) {
    	int dp[] = new int[amount+1];
    	Arrays.fill(dp, -1);
    	dp[0] = 0;
    	
    	for(int coin : coins) {
    		for(int i = 1; i <= amount; i++) {
    			if(i-coin >= 0 && dp[i-coin] != -1 && (dp[i] == -1 || dp[i-coin] + 1 < dp[i]))
    				dp[i] = dp[i-coin] + 1;
    		}
    	}
    	return dp[amount];
    }
    public static void main(String[] args) {
    	int coins[] = {1,2,5};
    	new Solution().coinChange(coins, 11);
    }
}
