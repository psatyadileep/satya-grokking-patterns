"""
https://leetcode.com/problems/reverse-linked-list/description/
LC 206 reverse Linked lIst


Explore:
1 can the LL be empty : yes
2.

Brianstorm :
1. Using two Pointers - O(n

Approach :
1. use a sentinel Node
2.




"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):

        if not head:
            return None


        prev = ListNode(0,head)
        curr = head
        while curr:
            next = curr.head
            curr.next  = prev
            prev = curr
            curr  = next

        return prev