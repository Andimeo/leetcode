class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int tank = 0;
        int num = 0;
        int start = 0;
        for (int p = 0 ; p < n + n - 1; p++) {
            int i = p % n;
            tank += gas[i] - cost[i];
            if (tank >= 0) {
                num++;
                if (num == n) {
                    return start;
                }
            } else {
                tank = 0;
                num = 0;
                start = i + 1;
            }
        }
        return -1;
    }
};
