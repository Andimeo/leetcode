package p331;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	public boolean isValidSerialization2(String preorder) {
		int numOfNulls = 0;
		int numOfNodes = 0;
		StringTokenizer st = new StringTokenizer(preorder, ",");
		while (st.hasMoreTokens()) {
			if (numOfNulls - numOfNodes == 1)
				return false;
			String token = st.nextToken();
			if ("#".equals(token))
				numOfNulls++;
			else
				numOfNodes++;
		}
		return numOfNulls - numOfNodes == 1;
	}

	public boolean isValidSerialization(String preorder) {
		StringTokenizer st = new StringTokenizer(preorder, ",");
		List<String> segs = new ArrayList<String>();
		int count = 0;
		while (st.hasMoreTokens()) {
			segs.add(st.nextToken());
		}
		for (int i = segs.size() - 1; i >= 0; i--) {
			if (segs.get(i).equals("#")) {
				count++;
			} else {
				if (count >= 2)
					count--;
				else
					return false;
			}
		}
		return count == 1;
	}

	public static void main(String[] args) {
		System.out.println(new Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"));
	}
}
