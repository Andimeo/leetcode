#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
    vector<int> v(n, 0);
    for (auto& b : bookings) {
      v[b[0] - 1] += b[2];
      if (b[1] < n)
	v[b[1]] -= b[2];
    }
    for (int i = 1; i < n ; i++) v[i] += v[i-1];
    return v;
  }
};
