from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0] * numCourses

        adj_list = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
            indegree[prereq] += 1

        q = deque()
        print(indegree)
        for key, val in enumerate(indegree):
            if val == 0:
                q.append(key)

        response = []
        while q:
            for _ in range(len(q)):

                course = q.popleft()
                response.append(course)

                prereqs = adj_list.get(course)

                for pre in prereqs:
                    indegree[pre] -= 1

                    if indegree[pre] == 0:
                        q.append(pre)

        return response[::-1]


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(Solution().findOrder(numCourses, prerequisites))