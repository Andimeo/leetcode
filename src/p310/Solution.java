package p310;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Solution {
	public List<Integer> findMinHeightTrees(int n, int[][] edges) {
		boolean visited[] = new boolean[n];
		int degs[] = new int[n];
		List<List<Integer>> graph = new ArrayList<List<Integer>>();
		for (int i = 0; i < n; i++) {
			graph.add(new ArrayList<>());
		}
		for (int[] edge : edges) {
			int x = edge[0], y = edge[1];
			graph.get(x).add(y);
			graph.get(y).add(x);
			degs[x]++;
			degs[y]++;
		}
		Queue<Integer> queue = new LinkedList<>();

		List<Integer> ans = new ArrayList<Integer>();
		do {
			ans.clear();
			while(!queue.isEmpty()) {
				int v = queue.poll();
				ans.add(v);
				for(int o : graph.get(v)) {
					degs[o]--;
				}
			}
			int min = Integer.MAX_VALUE;
			for (int i = 0; i < n; i++)
				if (!visited[i] && degs[i] < min)
					min = degs[i];
			for(int i = 0 ; i < n ; i++) {
				if(min == degs[i] && !visited[i]) {
					visited[i] = true;
					queue.add(i);
				}
			}
		} while (!queue.isEmpty());

		return ans;
	}

	public static void main(String[] args) {
		int edges[][] = { { 1, 0 }, { 0, 2 } };// , { 1, 3 } };
		// int edges[][] = { { 0, 3 }, { 1, 3 }, { 2, 3 }, { 4, 3 }, { 5, 4 } };
		for (int v : new Solution().findMinHeightTrees(3, edges))
			System.out.println(v);
	}

}
