"""
LC206
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Explore:
-> if not head: return None

Brainstorm:
-> Using tarversal


  prev       1-> 2 -> 3 -> 4 -> 5
 sentinel       next
Plan:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        sentinel = ListNode(0, head)
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

