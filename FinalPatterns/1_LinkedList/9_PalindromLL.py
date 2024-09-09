# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, current = None, head
        ll = DisplayLL(head)

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        ll_reverse = DisplayLL(prev)

        return ll_reverse == ll


def DisplayLL(head):
    ll_array = []
    while head:
        ll_array.append(head.val)
        head = head.next
    return ll_array

