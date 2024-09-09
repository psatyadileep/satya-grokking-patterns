"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Assumptions:
1. Can the array be empty : yes
2. Can only have a single head : return head


1 -> 9 -> 8 -> 3 -> 2 -> 10 -> 4
odd even
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        Sentinelodd = ListNode()
        Sentineleven = ListNode(0)


        sentinel = ListNode(0,Sentinelodd)
        curr = head
        count= 0
        while curr:
            count +=1
            if count%2 ==0 :
                Sentineleven.next = ListNode(curr.val)
                Sentineleven = Sentineleven.next
            else:
                Sentinelodd.next = ListNode(curr.val)
                Sentinelodd = Sentinelodd.next

            curr = curr.next


        Sentinelodd.next = Sentineleven

        return sentinel.next




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
ans = Solution().oddEvenList(a)

displayLL(a)

