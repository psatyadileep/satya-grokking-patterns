# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Observations:
-> you are given two lists
-> you should merge two lists into one

Edge cases:
-> one of the lists can be samller than
->once the both the lists are comapred until the equal lengths we basically apen dall the remaining elements
Algorithm :
-> have  pointers for both of the heads of the lists
-> iterate through both the lists
-> check which has a greater value and append the the node to result



"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode()

        tail = sentinel

        while list1 and list2:

            if list2.val >= list1.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        if list1:
            tail.next = list2

        return sentinel.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode()

        tail = sentinel

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return sentinel.next

