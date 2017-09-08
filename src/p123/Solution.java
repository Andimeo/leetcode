public class Solution {
    public int maxProfit(int[] prices) {
    	int n = prices.length;
    	if(n < 2)
    		return 0;
    	int[] left = new int[n];
    	int[] right = new int[n];
    	int low = prices[0];
    	left[0] = 0;
    	for(int i = 1; i < n; i++) {
    		left[i] = Math.max(0, prices[i] - low);
    		low = Math.min(low, prices[i]);
    	}
    	int high = prices[n - 1];
    	right[n - 1] = 0;
    	for(int i = n - 2 ; i >= 0; i--) {
    		right[i] = Math.max(0, high - prices[i]);
    		high = Math.max(high, prices[i]);
    	}

    	int[] leftMax = new int[n];
    	int[] rightMax = new int[n];
    	leftMax[0] = left[0];
    	rightMax[n-1] = right[n-1];
    	for(int i = 1 ; i < n ; i++)
    		leftMax[i] = Math.max(leftMax[i-1], left[i]);
    	for(int i = n - 2 ; i >= 0 ; i--)
    		rightMax[i] = Math.max(rightMax[i+1], right[i]);

    	int res = 0;
    	for(int i = 0; i < n; i++)
    		res = Math.max(leftMax[i] + rightMax[i], res);
    	return res;

    }
}