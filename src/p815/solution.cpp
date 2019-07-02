class Solution {
public:
  typedef pair<int, int> pi;
  int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
    if (T == S) return 0;
    int g[502][502];
    memset(g, 0, sizeof(g));
    int n = routes.size();
    for (int i = 0 ; i < n ; i++)
      sort(routes[i].begin(), routes[i].end());
        
    int rs = -1, rt = -1;
    for (int i = 0 ; i < n ; i++) {
      for (auto& s : routes[i]) {
	if (S == s) g[0][i+1] = 1;
	if (T == s) g[i+1][n + 1] = 1;
      }
    }
    for (int i = 0 ; i < n ; i++) {
      for (int j = i + 1; j < n ; j++) {
	int p = 0, q = 0;
	while (p < routes[i].size() && q < routes[j].size()) {
	  if (routes[i][p] < routes[j][q]) p++;
	  else if(routes[i][p] > routes[j][q]) q++;
	  else { g[i+1][j+1] = g[j+1][i+1] = 1; break;}
	}
      }
    }
    bool ok[502] = {false};
    queue<pi> q;
    q.push({0, 0});
    ok[0] = true;
    while (!q.empty()) {
      auto b = q.front();
      q.pop();
      if (b.first == n + 1) return b.second - 1;
      int v = b.first;
      for (int i = 0 ; i <= n + 1; i++) {
	if (!ok[i] && g[v][i]) {
	  q.push({i, b.second + 1});
	  ok[i] = true;
	}
      }
    }
    return -1;
  }
};
