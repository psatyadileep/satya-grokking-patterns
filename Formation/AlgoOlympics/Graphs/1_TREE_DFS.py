class Solution:


    def dfs(self,start_node,adj_list):

        def dfs_helper(curr_node):

            print(curr_node)

            neighbours = adj_list.get(curr_node)

            if not neighbours or len(neighbours)==0:
                print("Done")
                return


            for neighbur_node in neighbours:
                dfs_helper(neighbur_node)


        dfs_helper(start_node)


root_node = 10
adj_list = {
    10:[5,6,1],
    5:[2,3],
    6:[],
    1:[0],
    2:[],
    3:[],
    0:[],
}

Solution().dfs(root_node,adj_list)