class Solution {
public:
  int maxChunksToSorted(vector<int>& arr) {
    int n = arr.size();
    vector<int> min(n + 2, 0x7fffffff), max(n + 2, 0);
    for (int i = 1 ; i <= n; i++) {
      max[i] = max[i-1];
      if (arr[i-1] > max[i]) max[i] = arr[i-1];
    }
    for (int i = n ; i >= 1; i--) {
      min[i] = min[i+1];
      if (arr[i-1] < min[i]) min[i] = arr[i-1];
    }
        
    int result = 0;
    for (int i = 1; i <= n ; i++) {
      //cout << arr[i-1] << " " << max[i] << " " << min[i] << endl;
      if (max[i] <= min[i+1])
	result++;
    }
    return result;
  }
};
