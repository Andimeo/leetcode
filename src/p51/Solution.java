import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
	int[] row;
	int n;
	int hasFound;
	boolean[] col;
	List<String[]> res = new ArrayList<String[]>();
    public List<String[]> solveNQueens(int n) {
        row = new int[n];
        col = new boolean[n];
        this.n = n;
        DFS(0);
        return res;
    }
	private void DFS(int i) {
		if(i == n) {
			String[] r = new String[n];
			for(int j = 0 ; j < n; j++) {
				char[] s = new char[n];
				Arrays.fill(s, '.');
				s[row[j]] = 'Q';
				r[j] = new String(s);
			}
			res.add(r);
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
		new Solution().solveNQueens(7);
	}
}