#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  struct st {
    int state, steps, x, y;  
  };
  const int N = 2, M = 3, power = 6;
  int board2state(vector<vector<int>>& board) {
    int result = 0;
    for (auto& row : board) {
      for (auto& item : row) {
	result = result * power + item;
      }
    }
    return result;
  }
    
  vector<vector<int>> state2board(int state) {
    vector<vector<int>> result(N, vector<int>(M, 0));
    for (int i = N - 1; i >= 0 ; i--) {
      for (int j = M - 1; j >= 0; j--) {
	result[i][j] = state % power;
	state /= power;
      }
    }
    return result;
  }
    
  int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, -1, 0, 1};
  int slidingPuzzle(vector<vector<int>>& board) {
    st init;
    init.state = board2state(board);
    init.steps = 0;
    for (int i = 0 ; i < N; i++) {
      for (int j = 0; j < M; j++) {
	if (board[i][j] == 0) {
	  init.x = i;
	  init.y = j;
	}
      }
    }
    int final = 0;
    for (int i = 1; i <= power - 1; i++) {
      final = final * power + i;
    }
    final *= power;
        
    unordered_set<int> visited;
    queue<st> q;
    q.push(init);
    visited.insert(init.state);
    while (!q.empty()) {
      st cur = q.front();
      q.pop();
      if (cur.state == final) return cur.steps;
      vector<vector<int>> b = state2board(cur.state);
      for (int i = 0 ; i < 4; i++) {
	int nx = dx[i] + cur.x;
	int ny = dy[i] + cur.y;
	if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
	  swap(b[cur.x][cur.y], b[nx][ny]);
	  int nstate = board2state(b);
	  if (visited.count(nstate) == 0) {
	    //cout << nstate << endl;
	    visited.insert(nstate);
	    q.push({nstate, cur.steps + 1, nx, ny});
	  }
	  swap(b[cur.x][cur.y], b[nx][ny]);
	}
      }
    }
    return -1;
  }
};
