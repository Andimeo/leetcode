package p289;

public class Solution {
	int dx[] = { -1, -1, -1, 0, 0, 1, 1, 1 }, dy[] = { -1, 0, 1, -1, 1, -1, 0, 1 };

	public void gameOfLife(int[][] board) {
		if (board.length == 0)
			return;
		int n = board.length, m = board[0].length;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				board[i][j] *= 10;
				for (int k = 0; k < 8; k++) {
					int nx = i + dx[k];
					int ny = j + dy[k];
					if (nx >= 0 && nx < n && ny >= 0 && ny < m)
						board[i][j] += nx > i || nx == i && ny > j ? board[nx][ny] : board[nx][ny] / 10;
				}
			}
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (board[i][j] / 10 == 1) {
					if (board[i][j] % 10 == 2 || board[i][j] % 10 == 3)
						board[i][j] = 1;
					else
						board[i][j] = 0;
				} else {
					if (board[i][j] % 10 == 3)
						board[i][j] = 1;
					else
						board[i][j] = 0;
				}
	}

	public static void main(String[] args) {
		int b[][] = {{1,1},{1,0}};
		new Solution().gameOfLife(b);
		for(int i = 0 ; i < b.length; i++) {
			for(int j = 0 ; j < b[i].length; j++)
				System.out.print(b[i][j]);
			System.out.println();
		}

	}

}
