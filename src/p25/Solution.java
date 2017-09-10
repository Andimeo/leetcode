public class Solution {
	public ListNode reverseKGroup(ListNode head, int k) {
		int len = 0;
		ListNode p = head;
		while (p != null) {
			len++;
			p = p.next;
		}
		if (len == 0 || k > len || k == 1)
			return head;

		ListNode res = null;
		ListNode pre = null, cur = head, lastHead, lastTail = null, newHead, newTail;
		for (int group = 0; group < len / k; group++) {
			newTail = cur;
			ListNode next;
			for (int i = 0; i < k; i++) {
				next = cur.next;
				cur.next = pre;
				pre = cur;
				cur = next;
			}
			if (group == 0)
				res = pre;
			newHead = pre;
			if(group > 0)
				lastTail.next = newHead;
			lastHead = newHead;
			lastTail = newTail;
			pre = newTail;
		}
		lastTail.next = cur;
		return res;
	}
	public static void main(String[] args) {
	}
}