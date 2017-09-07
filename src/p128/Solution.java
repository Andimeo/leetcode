public class Solution {
    public int longestConsecutive(int[] num) {
        Set<Integer> set = new HashSet<Integer>();
        for(int c : num)
            set.add(c);
        int res = 0;
        for(int c : num) {
            int count = 1;
            int i = 1;
            while(set.contains(c+i)) {
                count++;
                set.remove(c+i);
                i++;
            }
            i = 1;
            while(set.contains(c-i)) {
                count++;
                set.remove(c-i);
                i++;
            }
            res = Math.max(res, count);
            set.remove(c);
        }
        return res;
    }
}