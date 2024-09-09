class Solution:


    def dfs(self,adj_list):
        visited = set()
        def dfs_helper(curr_node):
            visited.add(curr_node)
            print(curr_node)

            neighbours = adj_list.get(curr_node)

            if not neighbours or len(neighbours)==0:
                print("Done")
                return


            for neighbur_node in neighbours:

                if neighbur_node in visited:
                    continue
                dfs_helper(neighbur_node)

        for node in adj_list.keys():
            if not node in visited:
                dfs_helper(node)



adj_list = {
    10:[5],
    5:[2],
    6:[6],
    1:[0],
    2:[],
    3:[2,6],
    0:[1],
}

Solution().dfs(adj_list)