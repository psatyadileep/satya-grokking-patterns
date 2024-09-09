# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/description/
Observations:
-> you are given k sorted lists
-> The lists may not be of the same liength 
-> 


Visualization:
List 1: 1 -> 4 -> 5
List 2: 1 -> 3 -> 6
List 3: 2 -> 3 -> 7

Step 1: Merge list1 and list2
    merge1 : 1 -> 1 -> 2 -> 3 ->3 -> 4 ->5 ->6 -> 7
 Step 2 : Merge merge1 and list3

  mereg1 :1 -> 1 -> 2 -> 3 ->3 -> 4 ->5 ->6 -> 7

  List 3:  2 -> 3 -> 7
    merge 2 -> 1 -> 1 -> 2 ->  2 ->3-> 3 ->3 -> 4 ->5 ->6 -> 7-> 7


return 

Algorithm :
-> using the hlepr function to merge two lists

"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        
        while len(lists)>1:
            mergedlists = [] # will contains all the mreged lists

            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedlists.append(self.mergeLists(l1,l2))

            lists = mergedlists
        
        return lists[0]


    def mergeLists(self, l1 , l2): # Used to merge lists 
        
        dummy = ListNode()
        tail = dummy
        while l1 and l2:

            if l1.val> l2.val:
                tail.next = l2
                l2 = l2.next
                
            else:
                tail.next = l1
                l1 = l1.next
        
            tail = tail.next
        
        if l1:
            tail.next = l1
        
        if l2:
            tail.next = l2
        
        return dummy.next


    