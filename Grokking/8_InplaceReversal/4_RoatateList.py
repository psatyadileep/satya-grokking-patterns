"""
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


Explore:
-> if not head : return None

Brainstorm:
->Using two Pointers

   1 -> 2 -> 3 -> 4 -> 5
            slow     fas


         4-> 5 ->

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#      1-> 2 -> 3 -> 4 -> 5 ->
#              prev      curr





class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Calculate the length of the linked list
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        # Calculate the actual number of rotations needed (k % length)
        k = k % length

        # If k is 0, no rotation is needed
        if k == 0:
            return head

        # Find the new head and the new tail
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        curr = new_head
        while curr.next:
            curr = curr.next

        curr.next = head

        return new_head


