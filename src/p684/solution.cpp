class Solution {
public:
  int p[1004];
  int find(int x) {return x == p[x] ? x : p[x] = find(p[x]);}
  vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    for (int i = 0 ; i < 1004; i++) p[i] = i;
    for (auto& edge : edges) {
      int x = edge[0], y = edge[1];
      int px = find(x), py = find(y);
      if (px == py) return edge;
      p[py] = px;
    }
    return vector<int>{0, 0};
  }
};
