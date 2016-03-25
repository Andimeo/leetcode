package p321;

import java.util.Stack;

public class Solution {
	private int[] getMax(int[] nums, int n) {
		Stack<Integer> stack = new Stack<>();
		for (int i = 0; i < nums.length; i++) {
			while (!stack.empty() && stack.size() + nums.length - i > n && stack.peek() < nums[i])
				stack.pop();
			if (stack.size() < n)
				stack.push(nums[i]);
		}
		int[] ans = new int[n];
		for (int i = n - 1; i >= 0; i--)
			ans[i] = stack.pop();
		return ans;
	}

	public int[] maxNumber(int[] nums1, int[] nums2, int k) {
		int n = nums1.length, m = nums2.length;
		int[] ans = null;
		for (int i = 0; i <= n; i++) {
			if (k - i > m || k - i < 0)
				continue;
			int[] seq1 = getMax(nums1, i);
			int[] seq2 = getMax(nums2, k - i);
			int[] temp = merge(seq1, seq2);
			if (ans == null || !compare(ans, temp))
				ans = temp;
		}
		return ans;
	}

	private boolean compare(int[] ans, int[] temp) {
		for (int i = 0; i < ans.length; i++) {
			if (ans[i] < temp[i])
				return false;
			if (ans[i] > temp[i])
				return true;
		}
		return true;
	}

	private int[] merge(int[] seq1, int[] seq2) {
		int[] seq = new int[seq1.length + seq2.length];
		int i = 0, j = 0, k = 0;
		while (i < seq1.length && j < seq2.length)
			if (seq1[i] < seq2[j])
				seq[k++] = seq2[j++];
			else if(seq1[i] > seq2[j])
				seq[k++] = seq1[i++];
			else{
				if(compare(seq1, i, seq2, j) > 0)
					seq[k++] = seq1[i++];
				else
					seq[k++] = seq2[j++];
			}
		while (i < seq1.length)
			seq[k++] = seq1[i++];
		while (j < seq2.length)
			seq[k++] = seq2[j++];
		return seq;
	}

	private int compare(int[] seq1, int i, int[] seq2, int j) {
		int k = 0;
		for(; i + k < seq1.length && j + k < seq2.length; k++) {
			if(seq1[i+k] < seq2[j+k])
				return -1;
			if(seq1[i+k] > seq2[j+k])
				return 1;
		}
		if(i + k < seq1.length)
			return 1;
		if(j + k < seq2.length)
			return -1;
		return 0;
	}

	/*
	 * [2,5,6,4,4,0] [7,3,8,0,6,5,7,6,2] 15
	 */
	public static void main(String[] args) {
		int nums1[] = { 2, 5, 6, 4, 4, 0 }, nums2[] = { 7, 3, 8, 0, 6, 5, 7, 6, 2 };
		for (int n : new Solution().maxNumber(nums1, nums2, 15))
			System.out.println(n);
	}
}
