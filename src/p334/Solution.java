package p334;

public class Solution {
	public boolean increasingTriplet(int[] nums) {
		int min[] = new int[nums.length];
		int max[] = new int[nums.length];
		min[0] = nums[0];
		for (int i = 1; i < nums.length; i++)
			min[i] = Math.min(min[i - 1], nums[i]);
		max[nums.length - 1] = nums[nums.length - 1];
		for (int i = nums.length - 2; i >= 0; i--)
			max[i] = Math.max(max[i + 1], nums[i]);

		for (int i = 1; i + 1 < nums.length; i++) {
			if (min[i - 1] < nums[i] && nums[i] < max[i + 1])
				return true;
		}
		return false;
	}
}
