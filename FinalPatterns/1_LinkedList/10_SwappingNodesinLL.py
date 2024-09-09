"""
1721. Swapping Nodes in a Linked List
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

 se -> \1 -> 9 -> 8 -> 3 -> 2 -> 10 -> 4
 s, f


 se -> \1 -> 9 -> 8 -> 3 -> 2 -> 10 -> 4
   s           f

se -> \1 -> 9 -> 8 -> 3 -> 2 -> 10 -> 4    :    se -> \1 -> 9 -> 8 -> 3 -> 2 -> 10 -> 4
 s         f                                            s         f


 se -> \1 -> 9 -> 8 -> 3 -> 2 -> 10 -> 4     se -> \1 -> 9 -> 8 -> 3 -> 2 -> 10 -> 4
             s          f                                    s          f

 se -> \1 -> 9 -> 8 -> 3 -> 2 -> 10 -> 4
                            s          f

                             se -> \1 -> 9 -> 8 -> 3 -> 2 -> 10 -> 4
             s          f                                    s          f


Assumptions:


1. There may not be ahead
2. There can  only be a single node
2.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        sentinel = ListNode(0)
        sentinel.next = head
        slow = fast = sentinel

        for i in range(k):
            fast = fast.next

        first_kth_node = fast

        print(first_kth_node.val)



        while fast:
            fast = fast.next
            slow = slow.next
            print(fast.val, slow.val)



        pritn("test")
        second_kth_node = slow
        print(fast.val, slow.val)



        first_kth_node.val, second_kth_node.val = second_kth_node.val, first_kth_node.val


        return head

def displayLL(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

a = ListNode(1)
b = ListNode(9)
c = ListNode(8)
d = ListNode(3)
e = ListNode(2)
f = ListNode(10)
g = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

displayLL(a)
print(Solution().swapNodes(a,2))