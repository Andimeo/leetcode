package p324;

import java.util.Arrays;

public class Solution {
	public void wiggleSort(int[] nums) {
		int ans[] = Arrays.copyOf(nums, nums.length);
		Arrays.sort(ans);

		int t = 0;
		for (int i = (nums.length - 1) / 2, j = nums.length - 1; i >= 0; i--, j--) {
			if (j == (nums.length - 1) / 2)
				nums[t++] = ans[i];
			else {
				nums[t++] = ans[i];
				nums[t++] = ans[j];
			}
		}
	}
}
