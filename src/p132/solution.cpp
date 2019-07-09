class Solution {
public:
    int minCut(string s) {
        int n = s.length();
        vector<vector<bool>> palin(n, vector<bool>(n, false));
        for (int k = 1 ; k <= n ; k++) {
            for (int i = 0 ; i + k - 1 < n ; i++) {
                int j = i + k - 1;
                if (j == i || s[i] == s[j] && (i + 1 == j || palin[i+1][j-1]))
                    palin[i][j] = true;
            }
        }
        vector<int> dp(n, -1);
        dp[0] = 0;
        for (int i = 0; i < n ; i++) {
            for (int j = 0; j <= i; j++) {
                if (palin[j][i]) {
                    int cut = (j == 0 ? 0 : dp[j-1] + 1);
                    dp[i] = (dp[i] == -1 ? cut : min(dp[i], cut)); 
                }
            }
        }
        return dp[n-1];
    }
};
