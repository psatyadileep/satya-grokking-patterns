adj_list = {
    10:[5],
    5:[2],
    6:[5],
    1:[0],
    2:[],
    3:[2],
    0:[1]
}


def dfs(  adj_list):
    visited = set()


    def helper(curr):

        visited.add(curr)
        print(curr)

        neighbors = adj_list.get(curr)

        if not neighbors or len(neighbors) < 1:
            print("Done")
            return

        for neighbor in neighbors:
            if neighbor in visited:
                continue

            helper(neighbor)


    for node in adj_list.keys():
        if node not in visited:
            helper(node)



dfs(adj_list)
