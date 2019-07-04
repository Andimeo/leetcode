class Solution {
public:
    map<string, int> indexer;
    int index;
    int p[1000];
    double trans[1000];
    
    int find(int x) {
        if (x == p[x]) return x;
        int px = find(p[x]);
        trans[x] = trans[x] * trans[p[x]];
        p[x] = px;
        return px;
    }
    
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        for (int i = 0 ; i < 1000; i++) {
            p[i] = i;
            trans[i] = 1.0;
        }
        indexer.clear();
        index = 1;
        for (int i = 0 ;i < equations.size(); i++) {
            auto& eq = equations[i];
            for (auto& item : eq) {
                if (indexer.count(item) == 0)
                    indexer[item] = index++;
            }
            int a = indexer[eq[0]], b = indexer[eq[1]];
            int pa = find(a), pb = find(b);
            p[pa] = pb;
            trans[pa] = values[i] * trans[b] / trans[a];
        }
        vector<double> res;
        for (auto& query : queries) {
            int a = indexer[query[0]];
            int b = indexer[query[1]];
            if (!a || !b)  { res.push_back(-1.0); continue;}
            int pa = find(a), pb = find(b);
            if (pa != pb) res.push_back(-1.0);
            else res.push_back(trans[a] / trans[b]);
        }
        return res;
    }
};
