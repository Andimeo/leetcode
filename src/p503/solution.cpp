#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  map<int, int> m;
  stack<int> s;
  vector<int> nums;
  void func(int index, bool ok = false) {
    while(!s.empty()) {
      int v = s.top();
      if (nums[v] >= nums[index]) break;
      else {
	m[v] = index;
	s.pop();
      }
    }
    if (ok)
      s.push(index);
  }
  vector<int> nextGreaterElements(vector<int>& nums1) {
    nums = nums1;
    int n = nums.size();
    for (int i = 0 ; i < n; i++) {
      func(i, true);
    }
    for (int i = 0; i < n ; i++) {
      func(i);
    }
        
    while(!s.empty()) {
      m[s.top()] = -1;
      s.pop();
    }
    vector<int> res;
    for (int i = 0 ; i < n; i++)
      res.push_back(m[i] == -1 ? -1 : nums[m[i]]);
    return res;
  }
};
