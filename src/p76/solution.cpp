#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  string minWindow(string s, string t) {
    string ans = "";
    unordered_map<char, int> m, u;
    for (char c : t) {
      m[c]++;
    }
    bool ok[256] = {false};
    int start = 0;
    int num = 0;
    for (int i = 0 ; i < s.length(); i++) {
      if (m.count(s[i]) == 0) continue;
      u[s[i]]++;
      if (u[s[i]] >= m[s[i]] && !ok[s[i]]) {
	ok[s[i]] = true;
	num++;
      }
      while (start <= i && num == m.size()) {
	if (m.count(s[start]) == 0) {
	  start++;
	  continue;
	}
	u[s[start]]--;
	if (u[s[start]] < m[s[start]]) {
	  string tmp = s.substr(start, i - start + 1);
	  if (ans == "" || ans.length() > tmp.length()) ans = tmp;
	  ok[s[start]] = false;
	  num--;
	}
	start++;
      }
    }
    return ans;
  }
};
