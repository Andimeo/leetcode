class Solution {
public:
  void run(vector<int>& ans, string& s, int b, int e, int owner) {
    int level = 0;
    int start;
    for (int i = b; i <= e ; i++) {
      if (s[i] == '(') {
	if (level == 0) {
	  start = i;
	  ans[i] = owner;
	}
	level++;
      } else {
	level--;
	if (level == 0) {
	  run(ans, s, start + 1, i - 1, 1 - owner);
	  ans[i] = owner;
	}
      }
    }
  }
  vector<int> maxDepthAfterSplit(string seq) {
    int n = seq.length();
    vector<int> result(n, 0);
    run(result, seq, 0, n - 1, 0);
    return result;
  }
};
