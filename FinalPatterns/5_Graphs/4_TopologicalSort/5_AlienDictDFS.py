from collections import defaultdict


class Solution:
    def alienOrder(self, words):
        # Step 1: Build the graph (adjacency list) and in-degree count
        adj = defaultdict(list)
        visited = set()  # Tracks completely processed nodes
        path = set()  # Tracks nodes currently in the recursion stack
        order = []  # To store the topological order (reversed)

        # Initialize nodes in the graph for every unique character
        all_chars = set(''.join(words))

        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            min_length = min(len(first), len(second))

            # Edge case: if first word is a prefix of second word and longer, it's invalid
            if len(first) > len(second) and first[:min_length] == second[:min_length]:
                return ""

            # Find the first different character to determine the ordering
            for j in range(min_length):
                if first[j] != second[j]:
                    adj[first[j]].append(second[j])
                    break

        # Step 2: Perform DFS to detect cycles and determine topological sort
        def dfs(node):
            if node in path:  # Detected a cycle
                return True
            if node in visited:  # Node already fully processed
                return False

            path.add(node)  # Add to current recursion stack
            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True  # Cycle detected
            path.remove(node)  # Remove from current recursion stack
            visited.add(node)  # Mark as fully processed
            order.append(node)  # Add to the order stack

            return False  # No cycle detected

        # Run DFS from each unvisited node
        for char in all_chars:
            if char not in visited:
                if dfs(char):
                    return ""  # Cycle detected

        # Return the reversed order as the correct character sequence
        return ''.join(order[::-1])