public class Solution {
    public int firstMissingPositive(int[] A) {
        for(int i = 0 ; i < A.length; i++) {
            if(A[i] > 0 && A[i] < A.length && A[i] != i + 1) {
                if(A[i] != A[A[i]-1]){
                int t = A[i];
                A[i] = A[A[i] - 1];
                A[t-1] = t;
                i--;
                }
            }
        }
        for(int i = 0  ; i < A.length; i++)
        if(A[i] != i + 1)
                return i + 1;
        return A.length + 1;
    }
}