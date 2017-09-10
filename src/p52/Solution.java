
public class Solution {
	int[] row;
	int n;
	int hasFound;
	boolean[] col;
	int res;
    public int totalNQueens(int n) {
        row = new int[n];
        col = new boolean[n];
        this.n = n;
        DFS(0);
        return res;
    }
	private void DFS(int i) {
		if(i == n) {
			res++;
			return;
		}
		for(int j = 0; j < n ; j++) {
			if(!col[j]) {
				int k;
				for(k = 0 ; k < i; k++)
					if(Math.abs(i - k) == Math.abs(j - row[k]))
						break;
				if(k == i) {
					row[i] = j;
					col[j] = true;
					DFS(i+1);
					col[j] = false;
				}
			}
		}
	}
	public static void main(String[] args) {
		new Solution().totalNQueens(7);
	}
}