class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        """


        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node.next
        node.val =  temp.val
        node.next = temp.next

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
