"""
147. Insertion Sort List
Medium
Topics
Companies
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list.
 One element (red) is removed from the input data and inserted in-place into the sorted list with each iteratio
"""


#         self.
#         next = next


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode(0)
        sentinel.next=head
        prev =head
        curr= prev.next


        while curr:
            if curr.val>=prev.val:
                curr = curr.next
                prev = prev.next
                continue

            else:
                temp = sentinel
                while temp.next and temp.next.val<curr.val:
                    temp = temp.next

                prev.next =  curr.next
                next = temp.next
                curr.next = next
                temp.next = curr
                curr = prev.next



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


print("Original list:")
displayLL(a)

ans = Solution().insertionSortList(a)

print("List after removing duplicates:")
displayLL(ans)
