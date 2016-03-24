package p329;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Solution {
	class Pos {
		int x, y;

		public Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public int longestIncreasingPath(int[][] matrix) {
		if (matrix.length == 0 || matrix[0].length == 0)
			return 0;

		Map<Integer, List<Pos>> map = new TreeMap<>(new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				return o2 - o1;
			}
		});

		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[i].length; j++) {
				if (!map.containsKey(matrix[i][j]))
					map.put(matrix[i][j], new ArrayList<Pos>());
				map.get(matrix[i][j]).add(new Pos(i, j));
			}
		}
		int ans[][] = new int[matrix.length][matrix[0].length];
		for (int i = 0; i < ans.length; i++)
			Arrays.fill(ans[i], 1);

		Iterator<Integer> iter = map.keySet().iterator();
		iter.next();

		int result = 1;
		while (iter.hasNext()) {
			List<Pos> list = map.get(iter.next());
			for (Pos pos : list) {
				int x = pos.x, y = pos.y;
				ans[x][y] = highestAround(x, y, matrix, ans);
				result = Math.max(ans[x][y], result);
			}
		}
		return result;
	}

	private int highestAround(int x, int y, int matrix[][], int ans[][]) {
		int dx[] = { -1, 0, 1, 0 }, dy[] = { 0, -1, 0, 1 };
		int max = 1;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i], ny = y + dy[i];
			if (nx >= 0 && nx < matrix.length && ny >= 0 && ny < matrix[0].length && matrix[nx][ny] > matrix[x][y])
				max = Math.max(ans[nx][ny] + 1, max);
		}
		return max;
	}

	public static void main(String[] args) {
		int[][] input = { { 7, 7, 5 }, { 2, 4, 6 }, { 8, 2, 0 } };
		System.out.println(new Solution().longestIncreasingPath(input));
	}
}
