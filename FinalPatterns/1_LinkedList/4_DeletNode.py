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
                 
         sentinel -> 7  -> 8 -> 9 -> 10 -> 10 -> 10
                                    curr 
        
         sentinel -> 7  -> 8 -> 9 -> 10 -> 10
                                                curr 
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


        sentinel = ListNode()
        sentinel.next = head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e


curr = c

while curr:

    print(curr.val)
    curr = curr.next
