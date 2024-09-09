"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=m3b4alg7
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Assumtions:
1.can there be an empty list : tes
2. there can be only a single head


BrainSTorm
1. Using Two Pointers , Fast and Slow Pointers Approach

 1-> 2 -> 3 -> 4 -> 5

"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        sentinel = ListNode(0, head)
        fast = slow = sentinel

        for i in range(n):
            fast = fast.next


        while fast and fast.next:
            fast = fast.next
            slow  = slow.next

        if slow.next:
            slow.next = slow.next.next

        return sentinel.nexy

