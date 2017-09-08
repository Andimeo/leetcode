import java.util.Arrays;


public class Solution {

	boolean eleEqual(String a, String b) {
		char sa[] = a.toCharArray(), sb[] = b.toCharArray();
		Arrays.sort(sa);
		Arrays.sort(sb);
		return new String(sa).equals(new String(sb));
	}

	public boolean isScramble(String s1, String s2) {
		if (s1.length() != s2.length())
			return false;
		if (!eleEqual(s1, s2))
			return false;
		return back(s1, s2);
	}

	private boolean back(String s1, String s2) {
		if (s1.length() == 1 && s1.charAt(0) == s2.charAt(0))
			return true;
		boolean res = false;
		for (int i = 1; i < s1.length(); i++) {
			String t1 = s1.substring(0, i);
			String t2 = s2.substring(0, i);
			if (eleEqual(t1, t2)) {
				res = res || back(t1, t2) && back(s1.substring(i), s2.substring(i));
				if (res)
					break;
			}
			t2 = s2.substring(s2.length() - i);
			if (eleEqual(t1, t2)) {
				res = res || back(t1, t2) && back(s1.substring(i), s2.substring(0, s2.length() - i));
				if (res)
					break;
			}
		}
		return res;
	}

	public static void main(String[] args) {
		System.out.println(new Solution().isScramble("aa", "aa"));
	}
}