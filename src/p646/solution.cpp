#include<algorithm>

using namespace std;

class Solution {
public:
    static bool cmp(vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    }
    int findLongestChain(vector<vector<int>>& pairs) {
        int n = pairs.size();
        int *dp = new int[n];
        for(int i = 0; i < n; i++)
            dp[i] = 1;
        int result  = 1;
        sort(pairs.begin(), pairs.end(), Solution::cmp);
        for(int i = 1; i < n ; i++) {
            for(int j = 0; j < i; j++) {
                if(pairs[j][1] < pairs[i][0] && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                }
            }
            if(dp[i] > result)
                result = dp[i];
        }
        return result;
    }
};