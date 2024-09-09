class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()

        adj_list = collections.defaultdict(list)

        for key, val in edges:
            adj_list[key].append(val)
            adj_list[val].append(key)

        def helper(curr_node):
            if curr_node == destination:
                return True

            visited.add(curr_node)

            neighbors = adj_list.get(curr_node)

            if not neighbors or len(neighbors) == 0:
                return

            for neighbor in neighbors:
                if neighbor in visited:
                    continue

                if helper(neighbor):
                    return True

            return False

        return helper(source)

