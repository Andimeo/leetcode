class Solution {
public:
    bool ok[1000][1000];
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, -1, 0, 1};
    int n, m;
    void dfs(int x, int y, vector<vector<char>>& grid) {
        ok[x][y] = 1;
        for (int i = 0 ; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny] == '1' && !ok[nx][ny]) {
                dfs(nx, ny, grid);
            } 
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        n = grid.size();
        if (!n) return 0;
        m = grid[0].size();
        if (!m) return 0;
        int res = 0;
        memset(ok, 0, sizeof(ok));
        for (int i = 0 ; i < n ; i++) {
            for (int j = 0 ; j < m ; j++) {
                if (grid[i][j] == '1' && !ok[i][j]) {
                    res++;
                    dfs(i, j, grid);
                }
            }
        }
        return res;
    }
};
