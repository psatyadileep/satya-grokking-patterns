"""
https://leetcode.com/problems/possible-bipartition/
LC886
886. Possible Bipartition
Solved
Medium
Topics
Companies
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.



Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        count = n + 1
        colored = [-1] * count

        adjl = defaultdict(list)

        for a, b in dislikes:
            adjl[a].append(b)
            adjl[b].append(a)

        def bfs(source):
            q = collections.deque()

            colored[source] = 0

            q.append(source)

            while q:

                node = q.popleft()

                for dislike in adjl[node]:

                    if colored[dislike] == -1:
                        colored[dislike] = 1 - colored[node]
                        q.append(dislike)

                    elif colored[dislike] == colored[node]:
                        return False

            return True

        for i in range(1, n + 1):
            if colored[i] == -1:
                if not bfs(i):
                    return False

        return True



