# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Observations:
-> There are two lists with values that needs to be added
-> the linkedLists can be of variable lengths
->
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
Observations:
-> There are two lists with values that needs to be added

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
Observations:
-> There are two lists with values that needs to be added

"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            # 115 //10 = 11
            # 115%10 = 5
            carry = val // 10
            val = val % 10

            curr.next = ListNode(val)

            # update the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
