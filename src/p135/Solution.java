public class Solution {

    public int candy(int[] ratings) {
    	int n = ratings.length;
        int[] p = new int[n];
        p[0] = 1;
        for(int i = 1; i < n; i++) {
        	if(ratings[i] > ratings[i-1])
        		p[i] = p[i-1] + 1;
        	else
        		p[i] = 1;
        }
        int[] q = new int[n];
        q[n-1] = 1;
        for(int i = n - 2; i >= 0; i--) {
        	if(ratings[i] > ratings[i+1])
        		q[i] = q[i+1] + 1;
        	else
        		q[i] = 1;
        }

        int ans = 0;
        for(int i = 0 ; i < n ; i++) {
        	ans += Math.max(p[i], q[i]);
        }
        return ans;
    }

	public static void main(String[] args) {
		int[] p = new int[]{1, 101, 100, 4, 5};
		Solution sol = new Solution();
		System.out.println(sol.candy(p));
	}
}