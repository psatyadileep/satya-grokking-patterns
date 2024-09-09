"""
Geek loves linked list data structure. Given an array of integer arr of size n, Geek wants to construct the linked list from arr.

Construct the linked list from arr and return the head of the linked list.

GFG: https://practice.geeksforgeeks.org/problems/introduction-to-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=introduction-to-linked-list
"""


class Node:
    def __init__(self, data, next=None, prev=None):  # data -> value stored in node
        self.data = data
        self.next = next
        self.prev = prev


class Solution:

    def DisplayLL(self, head):

        curr = head

        while curr:
            print(curr.data, end="->")
            curr = curr.next

    def constructLL(self, arr):
        if not arr:
            return None

        head = Node(arr[0])
        prev = head

        for i in range(1, len(arr)):
            temp = Node(arr[i], None, prev)
            prev.next = temp
            prev = prev.next

        return head

    def DeleteHead(self, head):
        if not head or not head.next:
            return None

        prev = head

        head = head.next
        prev.next = None
        head.prev = None
        del prev

        return head

    # def DeletePrev(self, head):
    #     :Kth
    def deleteKth(self, n, head):
        if not head or n <= 0:
            return head

        if n == 1:
            return self.DeleteHead(head)

        curr = head
        pos = 1
        while curr and pos < n:
            curr = curr.next
            pos += 1

        if not curr:
            return head

        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev

        del curr

        return head










print(Solution().constructLL([19, 8, 7, 6, 6]))

LL2 = Solution().constructLL([5, 6, 7, 89, 10])

LL5 = Solution().constructLL([123,45,98, 13,17])
# ans = Solution().DeleteHead(LL2)
#
#
# LL3 = Solution().constructLL([123,45,98, 13,17])

Solution().DisplayLL(LL5)

ans = Solution().deleteKth(3,LL5)

Solution().DisplayLL(ans)

