#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<vector<int>> left, right, up, down;
  vector<vector<bool>> ok;
  string res = "";

  void dfs(int x, int y, int dx, int dy, string path) {
    ok[x][y] = true;
    if (x == dx && y == dy) {
      if (res == "" || res > path) res = path;
      return;
    }
    int nx, ny;
    nx = down[x][y];
    if (dx >= x && dx <= nx) nx = dx;
    if (!ok[nx][y])
      dfs(nx, y, dx, dy, path + "d");
    ny = left[x][y];
    if (dy >= ny && dy <= y) ny = dy;
    if (!ok[x][ny])
      dfs(x, ny, dx, dy, path + "l");
    ny = right[x][y];
    if (dy >= y && dy <= ny) ny = dy;
    if (!ok[x][ny])
      dfs(x, ny, dx, dy, path + "r");
    nx = up[x][y];
    if (dx >= nx && dx <= x) nx = dx;
    if (!ok[nx][y])
      dfs(nx, y, dx, dy, path + "u");
  }

  string findShortestWay(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
    int n = maze.size(), m = maze[0].size();
    left.assign(n, vector<int>(m, 0));
    right.assign(n, vector<int>(m, 0));
    up.assign(n, vector<int>(m, 0));
    down.assign(n, vector<int>(m, 0));
    ok.assign(n, vector<bool>(m, false));
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

    dfs(start[0], start[1], destination[0], destination[1], "");
    return ok[destination[0]][destination[1]] ? res : "impossible";
  }
};

int main(void) {
  vector<vector<int>> s;
  int a[][5] = {{0, 0, 0, 0, 0}, {1, 1, 0, 0, 1}, {0, 0, 0, 0, 0}, {0, 1, 0, 0, 1}, {0, 1, 0, 0, 0}};
  for (int i = 0 ; i < 5; i++) {
    s.push_back(vector<int>());
    for (int j = 0 ; j < 5; j++)
      s[i].push_back(a[i][j]);
  }
  //vector<int> start{4, 3}, destination{0, 1};
  vector<int> start{4, 3}, destination{3, 0};
  Solution sol;
  cout << sol.findShortestWay(s, start, destination) << endl;

  
  return 0;
}
