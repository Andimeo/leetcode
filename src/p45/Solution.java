public class Solution {
    public int jump(int[] A) {
    	int n = A.length;
    	int []dp = new int[n];
    	Arrays.fill(dp, Integer.MAX_VALUE);
    	dp[0] = 0;
    	int end = 1;
    	for(int i = 0; i < n - 1; i++ ) {
    		for(int j = end; j < n && j <= i + A[i] ; j++ ) {
    			dp[j] = Math.min(dp[j], dp[i] + 1);
    			end++;
    		}
    		if(end == n)
    			break;
    	}
        return dp[n-1];
    }
}