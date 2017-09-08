import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> fullJustify(String[] words, int L) {
        List<List<String>> tmp = new ArrayList<List<String>>();
        List<String> res = new ArrayList<String>();
        if(words == null || words.length == 0)
        	return res;
        int begin = 0, len = words[begin].length();
        List<String> cur = new ArrayList<String>();
        cur.add(words[0]);
        for(int i = 1; i < words.length; i++) {
        	if(len + words[i].length() + 1 <= L) {
        		len += words[i].length() + 1;
        		cur.add(words[i]);
        	}
        	else {
        		tmp.add(new ArrayList<String>(cur));
        		cur.clear();
        		cur.add(words[i]);
        		len = words[i].length();
        	}
        }
//        tmp.add(cur);
        for(List<String> l : tmp) {
        	res.add(pack(l, L));
        }
        StringBuilder sb = new StringBuilder();
        len = cur.get(0).length() + cur.size() - 1;
        sb.append(cur.get(0));
        for(int i = 1; i < cur.size(); i++) {
        	len += cur.get(i).length();
        	sb.append(" ");
        	sb.append(cur.get(i));
        }
        for(int i = len; i< L; i++)
        	sb.append(" ");
        res.add(sb.toString());
        return res;
    }

    private String pack(List<String> l, int L) {
    	StringBuilder sb = new StringBuilder();
    	if(l.size() == 1) {
    		sb.append(l.get(0));
    		for(int i = l.get(0).length(); i < L; i++)
    			sb.append(" ");
    		return sb.toString();
    	}
    	int len = l.size() - 1;
    	for(String s : l)
    		len += s.length();
    	int even = (L - len) / (l.size() - 1);
    	int mod = (L - len) % (l.size() - 1);
    	sb.append(l.get(0));
    	for(int i = 1; i < l.size(); i++) {
    		for(int j = 0 ; j <= even; j++)
    			sb.append(" ");
    		if(mod > 0) {
    			sb.append(" ");
    			mod--;
    		}
    		sb.append(l.get(i));
    	}
    	return sb.toString();
    }
}