
"""
Explore :
1. The LL maybe empty
2. There may not be two elemnst

Approach :
1. Use hash map
    add all elements to hashmap
    if a node retpeats return true else False

2. Use tortoise and hare matheod
    Have a slow nad fast pointer
    if sloow == fast
        return True

    else False

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        slow = fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False