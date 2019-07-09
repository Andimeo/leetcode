class Solution {
public:
  bool isValid(string s) {
    int level = 0;
    for (char c : s) {
      if (c == '(') level++;
      if (c ==')') level--;
      if (level < 0) break;
    }
    return level == 0;
  }
    
  vector<string> removeInvalidParentheses(string s) {
    vector<string> v;
    v.push_back(s);
    vector<string> result;
    while (true) {
      for (auto& ss : v) {
	if (isValid(ss)) {
	  result.push_back(ss);
	}
      }
      if (result.size() > 0) break;
      unordered_set<string> ok;
      vector<string> vv;
      for (auto& ss : v) {
	for (int i = 0 ; i < ss.length(); i++) {
	  if (ss[i] != '(' && ss[i] != ')') continue;
	  string ns = ss.substr(0, i) + ss.substr(i + 1, ss.length() - i - 1);
	  if (ok.count(ns) == 1) continue;
	  vv.push_back(ns);
	  ok.insert(ns);
	}
      }
      v = vv;
    }
    return result;
  }
};
