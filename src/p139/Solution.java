import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
    	int n = s.length();
        boolean dp[] = new boolean[n+1];
        for(int i = 1; i <= n; i++) {
        	for(int j = 0 ; j < i; j++) {
        		String sub = s.substring(j, i);
        		if(dict.contains(sub) && (j == 0 || dp[j])) {
        			dp[i] = true;
        			break;
        		}
        	}
        }
        return dp[n];
    }
    public static void main(String[] args) {
    	Solution sln = new Solution();
    	Set<String> set = new HashSet<String>(Arrays.asList("a", "b"));
    	System.out.println(sln.wordBreak("ab", set));
    }
}