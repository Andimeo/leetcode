class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int s2t[256];
        int t2s[256];
        int n = s.length();
        int m = t.length();
        if (n != m) return false;
        memset(s2t, -1, sizeof(s2t));
        memset(t2s, -1, sizeof(t2s));
        for (int i = 0; i < n; i++) {
            if (s2t[s[i]] == -1 && t2s[t[i]] == -1) {
                s2t[s[i]] = t[i];
                t2s[t[i]] = s[i];
            }
            else if (s2t[s[i]] != t[i] || t2s[t[i]] != s[i])
                return false;
        }
        return true;
    }
};
