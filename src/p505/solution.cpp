#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<vector<int>> left, right, up, down;
  vector<vector<int>> ok;

  void dfs(int x, int y, int dx, int dy, int dis) {
    ok[x][y] = dis;
    if (x == dx && y == dy) return;
    int ny = left[x][y];
    if (ny != y && (ok[x][ny] == -1 || ok[x][ny] > dis + y - ny))
      dfs(x, ny, dx, dy, dis + y - ny);
    ny = right[x][y];
    if (ny != y && (ok[x][ny] == -1 || ok[x][ny] > dis + ny - y))
      dfs(x, ny, dx, dy, dis + ny - y);
    int nx = up[x][y];
    if (nx != x && (ok[nx][y] == -1 || ok[nx][y] > dis + x - nx))
      dfs(nx, y, dx, dy, dis + x - nx);
    nx = down[x][y];
    if (nx != x && (ok[nx][y] == -1 || ok[nx][y] > dis + nx - x))
      dfs(nx, y, dx, dy, dis + nx - x);
  }

  int hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
    int n = maze.size(), m = maze[0].size();
    left.assign(n, vector<int>(m, 0));
    right.assign(n, vector<int>(m, 0));
    up.assign(n, vector<int>(m, 0));
    down.assign(n, vector<int>(m, 0));
    ok.assign(n, vector<int>(m, -1));
    for (int i = 0; i < n ; i++) {
      int one = -1;
      for (int j = 0; j < m ; j++) {
	if (maze[i][j] == 1) {
	  one = j;
	} else {
	  left[i][j] = one + 1;
	}
      }
    }
    for (int i = 0 ; i < n ; i++) {
      int one = m;
      for (int j = m - 1; j >= 0; j--) {
	if (maze[i][j] == 1) {
	  one = j;
	} else {
	  right[i][j] = one - 1;
	}
      }
    }
    for (int j = 0 ; j < m ; j++) {
      int one = -1;
      for (int i = 0 ; i < n ; i++) {
	if (maze[i][j] == 1) {
	  one = i;
	} else {
	  up[i][j] = one + 1;
	}
      }
    }
    for (int j = 0 ; j < m ; j++) {
      int one = n;
      for (int i = n - 1; i >= 0; i--) {
	if (maze[i][j] == 1) {
	  one = i;
	} else {
	  down[i][j] = one - 1;
	}
      }
    }

    dfs(start[0], start[1], destination[0], destination[1], 0);
    return ok[destination[0]][destination[1]];
  }
};

int main(void) {
  vector<vector<int>> s;
  int a[][5] = {{0, 0, 1, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 1, 0}, {1, 1, 0, 1, 1}, {0, 0, 0, 0, 0}};
  for (int i = 0 ; i < 5; i++) {
    s.push_back(vector<int>());
    for (int j = 0 ; j < 5; j++)
      s[i].push_back(a[i][j]);
  }
  vector<int> start{0, 4}, destination{4, 4};
  //vector<int> start{0, 4}, destination{3, 2};
  Solution sol;
  cout << sol.hasPath(s, start, destination) << endl;

  
  return 0;
}
