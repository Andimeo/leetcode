class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;
        int low = 0, high = n;
        while (low < high) {
            int mid = (low + high) >> 1;
            if (mid == 0 && nums[mid] > nums[mid + 1] || mid == n - 1 && nums[mid] > nums[mid - 1] || mid > 0 && mid < n - 1 && nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) {
                return mid;
            }
            
            if (mid == 0 && nums[mid] < nums[mid+1] || mid > 0 && nums[mid] > nums[mid-1] && nums[mid] < nums[mid+1]) 
                low = mid + 1;
            else
                high = mid;
        }
        return -1;
    }
};
