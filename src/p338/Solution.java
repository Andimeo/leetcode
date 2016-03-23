package p338;

import java.util.Arrays;
import java.util.function.IntConsumer;

public class Solution {
	public int[] countBits(int num) {
		if (0 == num) {
			return new int[] { 0 };
		}
		if (1 == num) {
			return new int[] { 0, 1 };
		}

		int[] ans = new int[num + 1];
		ans[0] = 0;
		ans[1] = 1;

		for (int i = 2; i <= num; i <<= 1) {
			for (int j = i; j <= num && j < 2 * i; j++) {
				ans[j] = 1 + ans[j - i];
			}
		}
		return ans;
	}

	public static void main(String[] args) {
		Arrays.stream(new Solution().countBits(2)).forEach(new IntConsumer() {
			@Override
			public void accept(int value) {
				System.out.println(value);
			}
		});
	}
}
