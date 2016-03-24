package p328;

public class Solution {

	public class ListNode {
		int val;
		ListNode next;

		ListNode(int x) {
			val = x;
		}
	}

	public ListNode oddEvenList(ListNode head) {
		recurse(head);
		return head;
	}
	
	class Struct{
		ListNode oddHead, oddTail, evenHead;
		public Struct(ListNode oh, ListNode ot, ListNode eh) {
			this.oddHead = oh;
			this.oddTail = ot;
			this.evenHead = eh;
		}
	}
	
	public Struct recurse(ListNode head) {
		if(head == null || head.next == null)
			return new Struct(head, head, null);
		
		if(head.next.next == null)
			return new Struct(head, head, head.next);
		
		ListNode odd = head, even = head.next;
		Struct s = recurse(head.next.next);
		odd.next = s.oddHead;
		s.oddTail.next = even;
		even.next = s.evenHead;
		return new Struct(odd, s.oddTail, even);
	}
}
