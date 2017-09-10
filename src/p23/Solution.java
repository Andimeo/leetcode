import java.util.List;
import java.util.Stack;

//class ListNode {
//	int val;
//	ListNode next;
//
//	ListNode(int x) {
//		val = x;
//		next = null;
//	}
//}

public class Solution {
	class Q implements Comparable<Q>{
		ListNode node;
		int value;
		public Q(ListNode n, int v) { node = n; value = v; }
		@Override
		public int compareTo(Q o) {
			return value - o.value;
		}
	}

	private ListNode merge(ListNode n1, ListNode n2) {
		if(n1 == null) return n2;
		if(n2 == null) return n1;
		ListNode res = new ListNode(-1), tmp = res;;
		ListNode p1 = n1, p2 = n2;
		while(p1 != null && p2 != null) {
			if(p1.val < p2.val) { res.next = p1; p1 = p1.next; }
			else { res.next = p2; p2 = p2.next; }
			res = res.next;
		}
		if(p1 != null)
			res.next = p1;
		if(p2 != null)
			res.next = p2;
		return tmp.next;
	}
	private int size(ListNode node) {
		int n = 0;
		while(node != null) {
			n++;node = node.next;
		}
		return n;
	}
	public ListNode mergeKLists(List<ListNode> lists) {
		if(lists.size() == 0)
			return null;
		PriorityQueue<Q> queue = new PriorityQueue<Q>();
		for(int i = 0 ; i < lists.size(); i++)
			queue.add(new Q(lists.get(i), size(lists.get(i))));
		while(queue.size() > 1 ) {
			Q q1 = queue.poll(), q2 = queue.poll();
			queue.add(new Q(merge(q1.node, q2.node), q1.value + q2.value));
		}
		return queue.poll().node;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		List<ListNode> list = new ArrayList<ListNode>();
		list.add(new ListNode(1));
		list.add(new ListNode(0));
		sol.mergeKLists(list);

	}
}