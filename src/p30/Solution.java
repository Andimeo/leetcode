import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
	public List<Integer> findSubstring(String S, String[] L) {
		Map<String, Integer> map = new HashMap<String, Integer>();
		for (String s : L)
			if (!map.containsKey(s))
				map.put(s, 1);
			else
				map.put(s, map.get(s) + 1);
		List<Integer> res = new ArrayList<Integer>();
		int len = L[0].length();
		for (int i = 0; i < len; i++) {
			int start = i, cnt = 0;
			Map<String, Integer> cur = new HashMap<String, Integer>();
			for (int end = start; end + len <= S.length(); end += len) {
				String s = S.substring(end, end + len);
				if (map.containsKey(s)) {
					if (cur.containsKey(s))
						cur.put(s, cur.get(s) + 1);
					else
						cur.put(s, 1);
					cnt++;

					if (cur.get(s) > map.get(s)) {
						for (int j = start;; j += len) {
							String t = S.substring(j, j + len);
							cur.put(t, cur.get(t) - 1);
							cnt--;
							if (t.equals(s)) {
								start = j + len;
								break;
							}
						}
					}
					if (cnt == L.length)
						res.add(start);
				} else {
					start = end + len;
					cnt = 0;
					cur.clear();
				}
			}
		}
		return res;
	}
	public static void main(String[] args) {
		System.out.println(new Solution().findSubstring("cbaccbcbbc", new String[]{"cb","bc"}));
	}
}