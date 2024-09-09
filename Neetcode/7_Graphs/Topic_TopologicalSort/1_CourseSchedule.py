import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()

        adj_list = collections.defaultdict(list)

        for source, dest in adj_list:

            adj_list[source].append(dest)



        toposort = []


        for edge in adj_list.keys():
            