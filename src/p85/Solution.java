import java.util.Arrays;
import java.util.Stack;

public class Solution {
	public int largestRectangleArea(int[] height) {
		Stack<Integer> stack = new Stack<Integer>();
		int i = 0;
		int maxArea = 0;
		int[] h = new int[height.length + 1];
		h = Arrays.copyOf(height, height.length + 1);
		while (i < h.length) {
			if (stack.isEmpty() || h[stack.peek()] <= h[i]) {
				stack.push(i++);
			} else {
				int t = stack.pop();
				maxArea = Math.max(maxArea, h[t] * (stack.isEmpty() ? i : i - stack.peek() - 1));
			}
		}
		return maxArea;
	}

	public int maximalRectangle(char[][] matrix) {
		int[][] num = new int[matrix.length][];
		for (int i = 0; i < matrix.length; i++) {
			num[i] = new int[matrix[i].length];
			for (int j = 0; j < matrix[i].length; j++)
				num[i][j] = matrix[i][j] == '1' ? 1 : 0;
		}
		for (int i = 1; i < matrix.length; i++)
			for (int j = 0; j < matrix[i].length; j++)
				if (num[i][j] == 1)
					num[i][j] += num[i - 1][j];
				else
					num[i][j] = 0;
		int res = 0;
		for (int i = 0; i < matrix.length; i++) {
			res = Math.max(res, largestRectangleArea(num[i]));
		}
		return res;
	}
}