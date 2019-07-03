class Solution {
public:
  int maxChunksToSorted(vector<int>& arr) {
    int count = 0;
    int max = -1;
    int n = arr.size();
    for (int i = 0; i < n; i++) {
      if (arr[i] > max)
	max = arr[i];
      if (i == max) count++;
    }
    return count;
  }
};
