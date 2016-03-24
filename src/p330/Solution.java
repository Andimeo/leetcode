package p330;

public class Solution {
	public int minPatches(int[] nums, int n) {
		long sum = 0;
		int patched = 0, i = 0;
		while (sum < n) {
			if(i >= nums.length || sum + 1 < nums[i]) {
				sum += sum + 1;
				patched++;
			} else {
				sum += nums[i];
				i++;
			}
		}
		return patched;
	}
}
