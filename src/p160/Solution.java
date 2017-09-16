public class Solution {
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		ListNode nA = headA, nB = headB;
		while(nA != null && nB != null) {
			nA = nA.next;
			nB = nB.next;
		}
		ListNode nC, nD;
		if(nA != null) {
			nC = headA;
			nD = headB;
			while(nA != null) {
				nA = nA.next;
				nC = nC.next;
			}
		} else {
			nC = headB;
			nD = headA;
			while(nB != null) {
				nB = nB.next;
				nC = nC.next;
			}
		}

		while(nC != null && nD != null) {
			if(nC.val == nD.val)
				return nC;
			nC = nC.next;
			nD = nD.next;
		}
		return nC;
	}
}