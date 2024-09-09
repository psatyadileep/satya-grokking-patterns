"""
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=problem-list-v2&envId=m3b4alg7


Explore:
1. Can the head be emoty : yes
2. There can be multiple elements of same value
3. There can only be a sigle  Node
4. can the node be repeted ore than twice ?


Brain Strom
1.    7  -> 8 -> 9 -> 10 -> 10 -> 11
     head

     sentinel -> 7  -> 8 -> 9 -> 10 -> 10 -> 10
                 curr

         sentinel -> 7  -> 8 -> 9 -> 10 -> 10 -> 10 -> 11
                                    curr    temp

         sentinel -> 7  -> 8 -> 9 -> 10 -> 10 -> 10 -> 11
                                    curr               temp


         sentinel -> 7  -> 8 -> 9 -> 10 -> 11
                                    curr   temp
                                              \
                                              \
2. take a sentinel node iterate the curr.next pointer until the
the next pointer pointer a value not eauqllaot the vaue of the current nide
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                # Skip all nodes with the same value
                temp = curr.next
                while temp and temp.val == curr.val:
                    temp = temp.next
                curr.next = temp
            else:
                curr = curr.next

        return sentinel.next

def displayLL(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

# Example usage
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(3)
f = ListNode(5)
g = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

print("Original list:")
displayLL(a)

ans = Solution().deleteDuplicates(a)

print("List after removing duplicates:")
displayLL(ans)
