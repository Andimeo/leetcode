int dp[2000 + 4][20000 + 4];

class Solution {
public:
    int longestArithSeqLength(vector<int>& A) {
      const int h = 10000;
      int n = A.size();
      for (int i = 0; i < 2004; i++)
        for (int j = 0 ; j < 20004; j++)
          dp[i][j] = 1;

      int result = 2;
      for (int i = 0 ; i < n ; i++)
        for (int j = 0; j < i; j++) {
          int d = a[i] - a[j] + h;
          dp[i][d] = dp[j][d] + 1;
          result = max(ans, dp[i][d]);
        }
      return result;
    }
};
