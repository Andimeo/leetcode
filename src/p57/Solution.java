import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Interval implements Comparable<Interval> {
	int start;
	int end;

	Interval() {
		start = 0;
		end = 0;
	}

	Interval(int s, int e) {
		start = s;
		end = e;
	}

	@Override
	public int compareTo(Interval o) {
		return this.start - o.start;
	}

}

public class Solution {
	public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
		intervals.add(newInterval);
		Collections.sort(intervals);
		List<Interval> res = new ArrayList<Interval>();
		res.add(intervals.get(0));
		for (int i = 1; i < intervals.size(); i++) {
			Interval cur = intervals.get(i), pre = res.get(res.size() - 1);
			if(cur.start >= pre.start && cur.start <= pre.end) {
				pre.end = Math.max(pre.end, cur.end);
			} else
				res.add(cur);
		}
		return res;
	}
}