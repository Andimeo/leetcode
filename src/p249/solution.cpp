#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string, vector<string>> hashmap;
        vector<vector<string>> res;
        
        for (int i = 0; i < strings.size(); ++i) {
            hashmap[calKey(strings[i])].push_back(strings[i]);
        }
        
        for (auto it = hashmap.begin(); it != hashmap.end(); ++it) {
            sort(it->second.begin(), it->second.end());
            res.push_back(it->second);
        }
        return res;
    }
private:
    string calKey(string input) {
      if (input.length() == 0) return input;
        string key = "a";
	int d = (input[0] - 'a' + 26) % 26 + 'a';
	for (int i = 1; i < input.length(); i++) {
	  int c = (input[i] - 'a' - d + 26) % 26 + 'a';
	  key += c;
	}
        return key;
    }
};

int main(void) {
  vector<string> strings = {"abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"};
  auto res = Solution().groupStrings(strings);
  for (auto& group : res) {
    for (auto& s: group) {
      cout << s << " ";
    }
    cout << endl;
  }
  return 0;
}
