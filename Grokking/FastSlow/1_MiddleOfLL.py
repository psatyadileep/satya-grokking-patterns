"""
LC876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Explore:
-> If not head return None

Brainstorm:
-> We can use fast and slow pointers
-> The idea is that while the fast pointer moves at 2x speed , The slow pointe only at hlf the speed
-> Therefore by the time fast pointer reaches the end , slow pointer will be in the middle



  [1,2,3,4,5]   - > [1,2,3,4,5]   ->        [1,2,3,4,5]
   SF                  s  F                      s   f

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_pointer = slow_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

