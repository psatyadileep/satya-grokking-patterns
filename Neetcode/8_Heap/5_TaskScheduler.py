import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        maxheap = Counter(tasks)

        heapq._heapify_max(maxheap)

