""""
https://leetcode.com/problems/middle-of-the-linked-list/description/
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3

Expllore:
-> can the array be emtpty yes

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


        sentinel = ListNode(0,head)
        temp = sentinel
        count = 0

        while temp.next:
            temp = temp.next
            count+=1

        mid = count//2 + 1

        temp = sentinel
        for i in range(1,mid+1):
            temp = temp.next


        return temp.val





LL1 = ListNode(1, ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
print(Solution().middleNode(LL1))



LL2= ListNode(1, ListNode(2,ListNode(3,ListNode(4))))
print(Solution().middleNode(LL2))


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


        slow  = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next




        return slow