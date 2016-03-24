package p331;

import java.util.StringTokenizer;

public class Solution {
	public boolean isValidSerialization(String preorder) {
		int numOfNulls = 0;
		int numOfNodes = 0;
		StringTokenizer st = new StringTokenizer(preorder, ",");
		while (st.hasMoreTokens()) {
			if(numOfNulls - numOfNodes == 1)
				return false;
			String token = st.nextToken();
			if ("#".equals(token))
				numOfNulls++;
			else
				numOfNodes++;
		}
		return numOfNulls - numOfNodes == 1;
	}
	
	public static void main(String[] args) {
		System.out.println(new Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"));
	}
}
