package p332;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class Solution {
	int sum = 1;
	List<String> ans;
	Map<String, Integer> map = new HashMap<>();
	List<String> cities;
	List<String> temp = new ArrayList<>();

	public List<String> findItinerary(String[][] tickets) {
		Set<String> set = new TreeSet<>();
		for (int i = 0; i < tickets.length; i++) {
			for (int j = 0; j < tickets[i].length; j++) 
				set.add(tickets[i][j]);
			sum++;
		}
		int n = set.size();
		cities = new ArrayList<>(set);
		for (int i = 0; i < n; i++)
			map.put(cities.get(i), i);

		int matrix[][] = new int[n][n];
		for (String[] ticket : tickets) {
			int from = map.get(ticket[0]);
			int to = map.get(ticket[1]);
			matrix[from][to]++;
		}

		int start = map.get("JFK");
		temp.add("JFK");
		DFS(start, 1, matrix);
		return ans;
	}

	private void DFS(int start, int has, int[][] matrix) {
		if(has == sum) {
			ans = new ArrayList<>();
			for(String s : temp)
				ans.add(s);
			return;
		}
		
		int n = matrix.length;
		for (int i = 0; i < n; i++) {
			if (matrix[start][i] > 0) {
				matrix[start][i]--;
				temp.add(cities.get(i));
				DFS(i, has+1, matrix);
				if(ans != null) {
					return;
				}
				matrix[start][i]++;
				temp.remove(temp.size() - 1);
			}
		}
	}

	public static void main(String[] args) {
		String[][] s = {{"MUC","LHR"},{"JFK","MUC"},{"SFO","SJC"},{"LHR","SFO"}};
		new Solution().findItinerary(s);
	}

}
