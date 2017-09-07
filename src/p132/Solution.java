import java.util.Arrays;

public class Solution {
	public int minCut(String s) {
		int n = s.length();
		boolean[][] palin = new boolean[n][];
		for (int i = 0; i < n; i++) {
			palin[i] = new boolean[n];
			palin[i][i] = true;
		}
		for (int l = 2; l <= n; l++) {
			for (int i = 0; i < n; i++) {
				int e = Math.min(n - 1, i + l - 1);
				palin[i][e] = s.charAt(i) == s.charAt(e) && (i + 1 >= e - 1 || palin[i + 1][e - 1]);
			}
		}

		int[] d = new int[n + 1];
		Arrays.fill(d, -1);
		d[0] = 0;

		boolean[] g = new boolean[n+1];
		for (int i = 0; i < n; i++) {
			int vertex = -1;
			int dist = Integer.MAX_VALUE;
			for (int j = 0; j <= n; j++) {
				if (!g[j] && d[j] != -1 && d[j] < dist) {
					vertex = j;
					dist = d[j];
				}
			}
			g[vertex] = true;
			if(vertex >= n)
				continue;
			for (int j = 1; j <= n; j++) {
				if (palin[vertex][j-1] && (d[j] == -1 || d[j] > d[vertex] + 1))
					d[j] = d[vertex] + 1;
			}
		}
		return d[n] - 1;
	}

	public static void main(String[] args) {
		System.out.println(new Solution().minCut("aabbccc"));
	}
}