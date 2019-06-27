
using namespace std;

class Solution {
public:
  vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    map<int, int> m;
    stack<int> s;
    for (int num : nums2) {
      while(!s.empty()) {
	int v = s.top();
	if (v > num) break;
	else {
	  m[v] = num;
	  s.pop();
	}
      }
      s.push(num);
    }
    while(!s.empty()) {
      m[s.top()] = -1;
      s.pop();
    }
    vector<int> res;
    for (int num : nums1)
      res.push_back(m[num]);
    return res;
  }
};
