"""
https://leetcode.com/problems/course-schedule/?envType=problem-list-v2&envId=a9fsdycj
207. Course Schedule
So
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjl = defaultdict(list)

        for course, prereq in prerequisites:
            adjl[course].append(prereq)

        visited = set()

        path = set()

        def dfs(course):

            if course in path:
                return False

            if course in visited:
                return True

            visited.add(course)
            path.add(course)

            for prereq in adjl[course]:
                if not dfs(prereq):
                    return False

            path.remove(course)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False

        return True

