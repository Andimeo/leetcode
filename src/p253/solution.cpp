/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
  bool cmp(Interval& a, Interval& b) {
    return a.start < b.start;
  }
  int minMeetingRooms(vector<Interval>& intervals) {
    sort(intervals.begin(), intervals.end(), cmp);
    multiset<int> st;
    int res = 0;
    for(auto val: intervals) {
      while(!st.empty() && val.start >= *st.begin()) st.erase(st.begin());
      st.insert(val.end);
      res = max(res, (int)st.size());
    }
    return res;
  }
};
