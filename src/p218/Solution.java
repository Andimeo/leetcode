package p218;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
	public List<int[]> getSkyline(int[][] buildings) {
		Queue<Integer> q = new PriorityQueue<>((a, b) -> (b - a));
		List<int[]> lines = new ArrayList<>();
		List<int[]> result = new ArrayList<>();
		for (int[] building : buildings) {
			int l = building[0], r = building[1], h = building[2];
			lines.add(new int[] { l, -h });
			lines.add(new int[] { r, h });
		}
		lines.sort((a, b) -> (a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]));
		q.add(0);
		int prev = 0;
		for (int[] l : lines) {
			if (l[1] < 0)
				q.add(-l[1]);
			else
				q.remove(l[1]);
			int cur = q.peek();
			if (cur != prev) {
				result.add(new int[] { l[0], cur });
				prev = cur;
			}
		}
		return result;
	}
}
