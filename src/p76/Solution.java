public class Solution {
    public String minWindow(String S, String T) {
        int ls = S.length(), lt = T.length();
        int cT[] = new int[256],fT[] = new int[256];
        for(int i = 0 ; i < lt; i++)
        	cT[T.charAt(i)]++;
        int hasFound = 0;
        int winStart = -1, winEnd = ls;
        for(int i = 0, start = 0 ; i < ls; i++) {
        	if(cT[S.charAt(i)] != 0) {
        		fT[S.charAt(i)]++;
        		if(fT[S.charAt(i)] <= cT[S.charAt(i)]) hasFound++;
        		if(hasFound == lt) {
        			while(cT[S.charAt(start)] == 0 || fT[S.charAt(start)] > cT[S.charAt(start)]) {
        				if(cT[S.charAt(start)] != 0)
        					fT[S.charAt(start)]--;
        				start++;
        			}
        			if(winEnd - winStart > i - start) {
        				winStart = start;
        				winEnd = i;
        			}
        			fT[S.charAt(start)]--;
        			start++;
        			hasFound--;
        		}
        	}
        }
        return winStart != -1 ? S.substring(winStart, winEnd + 1) : "";
    }
}