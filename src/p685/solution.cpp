class Solution {
public:
  int deg[1004];
  int p[1004];
  int find(int x) { return x == p[x] ? x : p[x] = find(p[x]); }
  vector<int> isValid(vector<vector<int>>& edges, int remove) {
    for (int i = 0; i < 1004; i++) p[i] = i;
    for (int i = 0 ; i < edges.size(); i++) {
      if (i == remove) continue;
      int x = edges[i][0], y = edges[i][1];
      int px = find(x), py = find(y);
      if (px == py) return edges[i];
      p[px] = py;
    }
    return vector<int>();
  }
    
  vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
    memset(deg, 0, sizeof(deg));
    for (auto& edge : edges) {
      int x = edge[0], y = edge[1];
      deg[y]++;
    }
    int point = -1;
    for (int i = 1 ; i < 1004; i++) {
      if (deg[i] > 1) {
	point = i;
	break;
      }
    }

    if (point != -1) {
      for (int i = edges.size() - 1 ; i >= 0; i--) {
	if (edges[i][1] == point) {
	  vector<int> r = isValid(edges, i);
	  if (r.size() == 0) return edges[i];
	}
      }
      return vector<int>{0, 0};
    } else {
      return isValid(edges, -1);
    }
  }
};
