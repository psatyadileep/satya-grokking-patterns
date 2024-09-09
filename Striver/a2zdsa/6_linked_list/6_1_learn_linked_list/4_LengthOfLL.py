"""
Geek loves linked list data structure. Given an array of integer arr of size n, Geek wants to construct the linked list from arr.

Construct the linked list from arr and return the head of the linked list.

GFG: https://practice.geeksforgeeks.org/problems/introduction-to-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=introduction-to-linked-list
"""


class Node:
    def __init__(self, data,next= None):   # data -> value stored in node
        self.data = data
        self.next = next

class Solution:



    def DisplayLL(self,head):

        curr = head

        while curr:
            print(curr.data,end="->")
            curr = curr.next


    def constructLL(self, arr):
        if not arr:
            return None

        head = Node(arr[0])

        curr = head

        for i in range(1,len(arr)):

            temp = Node(arr[i])
            curr.next = temp
            curr = curr.next


        return head

    def LegthOfLl(self,head):

        count = 0
        if not head:
            return count

        curr = head
        while curr:
            count+=1
            curr = curr.next

        return count


ans  = Solution().constructLL([19,8,7,6,6])
print(ans.data)
print(Solution().LegthOfLl(ans))

