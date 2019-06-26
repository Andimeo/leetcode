#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int lengthOfLongestSubstringKDistinct(string s, int k) {
    map<char, int> m;
    int start = 0;
    int res = 0;
    for (int i = 0 ; i < s.length(); i++) {
      m[s[i]]++;
      if (m.size() > k) {
	while(m.size() > k) {
	  m[s[start]]--;
	  if (m[s[start]] == 0)
	    m.erase(s[start]);
	  start++;
	}
      } else {
	res = max(res, i - start + 1);
      }
    }
    return res;
  }
};

int main(void) {
  Solution s;
  cout << s.lengthOfLongestSubstringKDistinct("eceba", 2) << endl;
  cout << s.lengthOfLongestSubstringKDistinct("", 2) << endl;
  cout << s.lengthOfLongestSubstringKDistinct("a", 1) << endl;
  cout << s.lengthOfLongestSubstringKDistinct("a", 0) << endl;
  cout << s.lengthOfLongestSubstringKDistinct("", 0) << endl;
  return 0;
}
