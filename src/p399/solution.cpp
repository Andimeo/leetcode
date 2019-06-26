class Solution {
public:

  double graph[1000][1000];
  bool ok[1000][1000];
  map<string, int> indexer;
  int index;
    
  bool color[1000];
  double ans;
  void dfs(int a, int b, double v) {
    if (a == b) {
      ans = v;
      return;
    }
    color[a] = true;
    for (int i = 1; i < index; i++) {
      if (!color[i] && ok[a][i]) {
	dfs(i, b, graph[a][i] * v);
      }
    }
  }
    
  vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
    indexer.clear();
    index = 1;
    memset(ok, 0, sizeof(ok));
    for (int i = 0 ;i < equations.size(); i++) {
      auto& eq = equations[i];
      for (auto& item : eq) {
	if (indexer.count(item) == 0)
	  indexer[item] = index++;
      }
      int a = indexer[eq[0]], b = indexer[eq[1]];
      graph[a][b] = values[i];
      graph[b][a] = 1. / values[i];
      ok[a][b] = ok[b][a] = true;
    }
    vector<double> res;
    for (auto& query : queries) {
      int a = indexer[query[0]];
      int b = indexer[query[1]];
      if (a == 0 || b == 0)
	res.push_back(-1.);
      else {
	memset(color, 0, sizeof(color));
	ans = -1.;
	dfs(a, b, 1.);
	res.push_back(ans);
      }
    }
    return res;
  }
};
