import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class Solution {
	private List<String> list = new ArrayList<String>();
	private String oriStr;
	private Set<String> dict;
	private List<String> res = new ArrayList<String>();
	private List<List<Integer>> index = new ArrayList<List<Integer>>();

	public List<String> wordBreak(String s, Set<String> dict) {
		oriStr = s;
		this.dict = dict;
		for (int i = 0; i <= s.length(); i++)
			index.add(new ArrayList<Integer>());
		for (int i = 0; i < s.length(); i++) {
			for (int j = i; j < s.length(); j++) {
				if (dict.contains(s.substring(i, j + 1)))
					index.get(j + 1).add(i);
			}
		}
		back(s.length());
		return res;
	}

	private void back(int i) {
		if (i == 0) {
			String ans = "";
			for (int j = list.size() - 1; j >= 0; j--)
				ans = ans + list.get(j) + " ";
			res.add(ans.substring(0, ans.length() - 1));
			return;
		}

		for (int j = 0; j < index.get(i).size(); j++) {
			int k = index.get(i).get(j);
			list.add(oriStr.substring(k, i));
			back(k);
			list.remove(list.size() - 1);
		}
	}

}