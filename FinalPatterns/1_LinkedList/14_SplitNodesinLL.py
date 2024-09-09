"""
https://leetcode.com/problems/split-linked-list-in-parts/description/
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Count the total number of nodes
        total_length = 0
        curr = head
        while curr:
            total_length += 1
            curr = curr.next

        # Step 2: Calculate the size of each part and the number of larger parts
        part_size = total_length // k
        extra_parts = total_length % k

        # Step 3: Split the list
        result = []
        curr = head
        for i in range(k):
            part_head = curr
            part_length = part_size + (1 if i < extra_parts else 0)
            for j in range(part_length - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_part_head = curr.next
                curr.next = None
                curr = next_part_head
            result.append(part_head)

        # Step 4: If there are more parts than nodes, append None to the result
        while len(result) < k:
            result.append(None)

        return result


