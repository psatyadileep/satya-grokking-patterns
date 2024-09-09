# class ListNode:
#     def __init__(self, key,val):
#         self.key , self.val = key, val
#         self.next = self.prev = None
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}
#         # Left is the least recrntly
#         # right is the most recently used
#
#
#         self.left , self.right = ListNode(0,0), ListNode(0,0)
#         self.left.next = self.right
#         self.right.prev  = self.left
#
#
#     def remove(self,node):
#
#
#     def insert(self, node):
#     def get(self, key: int) -> int:
#         if key in  self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key]
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#
#         if key in  self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = ListNode(key,value)
#         self.insert(self.cache[key])
#
#         if len(self.cache)>self.cap:
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]
#             ## remove least recrntly used
#
#
# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)