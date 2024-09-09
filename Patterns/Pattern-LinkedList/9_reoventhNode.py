"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
19. Remove Nth Node From End of List

"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a sentinel node
        sentinel = ListNode(0)
        sentinel.next = head
        slow = fast = sentinel

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both slow and fast until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        if slow.next:
            slow.next = slow.next.next

        # Return the modified list starting from sentinel.next
        return sentinel.next

