class Solution:
    def canFinish(self, N, arr):
        adj = defaultdict(list)

        for course, prereq in arr:
            adj[course].append(prereq)

        visited = set()
        path = set()

        def dfs(node, path):
            if node in path:
                return True

            if node in visited:
                return False

            visited.add(node)
            path.add(node)

            for prereq in adj[node]:
                if prereq in path:
                    return True

                else:
                    if dfs(prereq, path):
                        return True

            path.remove(node)
            return False

        for i in range(N):
            if i not in visited:
                if dfs(i, path):
                    return False

        return True


