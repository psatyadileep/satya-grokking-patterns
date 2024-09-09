
adj_list = {
    10:[5,6,1],
    5:[2,3],
    6:[],
    1:[],
    2:[],
    3:[],
    0:[]
}

root_node = 10



def dfs(root,adj_list):
    visited= set()
    def helper(curr):

        print(curr)

        neighbors = adj_list.get(curr)

        if not neighbors or len(neighbors)<1:
            print("Done")
            return

        for neighbor in neighbors:

            helper(neighbor)


    helper(root)


dfs(root_node,adj_list)
