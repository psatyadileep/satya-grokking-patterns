"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


Observations:
-> every single node has a random pointer to another node in the lsit
-> We have to look into how to create a link to the subsequent nodes

Edge cases:
-> The node might to another node which is not yet created
-> the node might point to None which is not a node

Algorithm:
-> We will use two passes
-> we will use a hash to store a maps of old and their new node copies
-> Iterate through the old list while mapping them and creating copy nodes witjout any links
-> now iterate the second time linking the next and random pointers using the hashmap
-> retrive the first head in the copy list using map[head]
-> make sure the None edge case is handled in the hasmp

"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_to_new_map = {None: None}

        curr = head

        while curr:
            copy = Node(curr.val)
            old_to_new_map[curr] = copy

            curr = curr.next

        curr = head

        while curr:
            copy = old_to_new_map[curr]
            curr.next = old_to_new_map[curr.next]
            curr.random = old_to_new_map[curr.random]

            curr = curr.next

        return old_to_new_map[head]