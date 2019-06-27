#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<vector<int>> dp;
  int go(int s, int e, vector<int>& nums, int sum) {
    if (dp[s][e] != -1) return dp[s][e];
    if (s == e) return dp[s][e] = nums[s];
    int v1 = nums[s] + sum - go(s + 1, e, nums, sum - nums[s]);
    int v2 = nums[e] + sum - go(s, e - 1, nums, sum - nums[e]);
    return dp[s][e] = max(v1, v2);
  }
    
  bool PredictTheWinner(vector<int>& nums) {
    int n = nums.size();
    dp.assign(n, vector<int>(n, -1));
    int sum = accumulate(nums.begin(), nums.end(), 0);
    int v = go(0, n - 1, nums, sum);
    return v * 2 >= sum;
  }
};
