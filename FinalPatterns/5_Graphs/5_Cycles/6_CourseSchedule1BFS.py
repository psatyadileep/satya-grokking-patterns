"""
https://leetcode.com/problems/course-schedule/description/
207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create the adjacency list and indegree array
        adj = defaultdict(list)
        indegree = [0] * numCourses

        # Build the graph
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        # Initialize the queue with all courses having indegree of 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        response = []

        # Process courses in topological order
        while q:
            node = q.popleft()
            response.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # If the response size equals the number of courses, return True
        return len(response) == numCourses