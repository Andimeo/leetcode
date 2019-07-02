class Solution {
public:
  set<string> seen;
  string ans;
  string crackSafe(int n, int k) {
    if (n == 1 && k == 1) return "0";
    string s = "";
    for (int i = 0 ; i + 1 < n ; i++) {
      s = s + "0";
    }
        
    ans = "";
    dfs(s, k);
    ans = ans + s;
    return ans;
  }
    
  void dfs(string node, int k) {
    int n = node.length();
    for (int i = 0 ; i < k ; i++) {
      string next = node + string(1, '0' + i);
      if (seen.count(next) == 0) {
	cout << next << endl;
	seen.insert(next);
	dfs(next.substr(1, n), k);
	ans = ans + string(1, '0' + i);
      }
    }
  }
};
