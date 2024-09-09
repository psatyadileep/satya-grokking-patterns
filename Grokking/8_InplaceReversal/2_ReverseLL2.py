""""
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/
Given the head of a singly linked list and two integers left and right w
here left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Approach :
-> the idea is to first move iterate to i-1  node , so we point to the ith node
->    prev ->  1- > 2       ->3 -> 4 -> 5
            prev    start
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        leftprev = dummy
        curr = head

        for i in range(left-1):
            leftprev = curr
            curr = curr.next

        prev = None
        for i in range(right - left +1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        leftprev.next.mext = curr
        leftprev.next = prev
        return dummy.next
