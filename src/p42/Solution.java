package p42;

public class Solution {
    public int trap(int[] A) {
        int n = A.length;
        if(n < 3)
            return 0;
        int leftMax[] = new int [n];
        int rightMax[] = new int [n];
        leftMax[0] = 0;
        rightMax[n-1] = 0;
        for(int i = 1 ; i < n; i++ )
            leftMax[i] = Math.max(leftMax[i-1], A[i-1]);
        for(int i = n - 2 ; i >= 0 ; i--)
            rightMax[i] = Math.max(rightMax[i+1], A[i+1]);
        int res = 0;
        for(int i = 1; i < n - 1; i++)
            res += Math.max(0, Math.min(rightMax[i], leftMax[i]) - A[i]);
        return res;
    }
}