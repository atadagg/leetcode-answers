/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {		

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

		ListNode answer = new ListNode();
		ListNode tmp;
		int i = 0;
		int remainder = 0;
		
		tmp = answer;
		while(l1 != null || l2 != null) {
			
			if(l1 == null) {
				answer.next = new ListNode((l2.val + remainder) % 10);
				answer = answer.next;
				remainder = (int) ((l2.val + remainder) / 10);
				l2 = l2.next;
			} else if (l2 == null) {
				answer.next = new ListNode((l1.val + remainder) % 10);
				answer = answer.next;
				remainder = (int) ((l1.val + remainder) / 10);
				l1 = l1.next;
			} else {
				answer.next = new ListNode((l1.val + l2.val + remainder) % 10);
				answer = answer.next;
				remainder = (int) ((l1.val + l2.val + remainder) / 10);
				l1 = l1.next;
				l2 = l2.next;
			}
			System.out.println(answer.val);
		}

        		if(remainder != 0) {
			answer.next = new ListNode(remainder);
			answer = answer.next;
		}
	
		return tmp.next;
		
		

	}
}
