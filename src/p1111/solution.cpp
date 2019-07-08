class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int n = seq.length();
        vector<int> result(n, 0);
        int level = 0;
        for (int i = 0; i < n ; i++) {
            if (seq[i] == '(') {
                if (level++ % 2 == 1) result[i] = 1;
            } else {
                if (--level % 2 == 1) result[i] = 1;
            }
        }
        return result;
    }
};
